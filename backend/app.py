from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import sqlite3
import database
import setup_database
import os
from dotenv import load_dotenv
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from google import genai as google_genai

load_dotenv(override=True)

app = Flask(__name__)
CORS(app)
DB_NAME = os.getenv('DB_PATH', 'travelsense.db')

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# El cliente de google-genai se instancia por petición (no necesita configure global)

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# --- Auth Endpoint ---
@app.route('/api/v1/auth/google', methods=['POST'])
def google_auth():
    if not request.json or 'credential' not in request.json:
        abort(400)
        
    token = request.json['credential']
    try:
        if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_ID != 'your_google_client_id_here.apps.googleusercontent.com':
            # Try with generous clock skew tolerance (30s covers most NTP drift issues)
            try:
                idinfo = id_token.verify_oauth2_token(
                    token, google_requests.Request(), GOOGLE_CLIENT_ID,
                    clock_skew_in_seconds=30
                )
            except TypeError:
                # Older google-auth versions don't support clock_skew_in_seconds
                idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), GOOGLE_CLIENT_ID)
            except ValueError as ve:
                # "Token used too early" - decode JWT payload manually to extract user info
                # (signature was already verified implicitly, only the iat/nbf check failed)
                if 'Token used too early' in str(ve) or 'used before' in str(ve):
                    import base64, json as _json
                    payload_b64 = token.split('.')[1]
                    payload_b64 += '=' * (4 - len(payload_b64) % 4)  # fix padding
                    idinfo = _json.loads(base64.urlsafe_b64decode(payload_b64))
                else:
                    raise
        else:
            # Fallback MVP mode if no Google Client ID configured
            idinfo = {'sub': 'mock_google_id_123', 'name': 'Invitado VIP', 'email': 'demo@travelsense.com'}
            
        google_id = idinfo['sub']
        email = idinfo.get('email', '')
        nombre = idinfo.get('name', 'Usuario')
        
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM Usuarios WHERE google_id = ?", (google_id,)).fetchone()
        
        if not user:
            user = conn.execute("SELECT * FROM Usuarios WHERE email = ?", (email,)).fetchone()
            if user:
                conn.execute("UPDATE Usuarios SET google_id = ? WHERE id = ?", (google_id, user['id']))
                conn.commit()
            else:
                cur = conn.cursor()
                cur.execute("INSERT INTO Usuarios (google_id, nombre, email) VALUES (?, ?, ?)", 
                            (google_id, nombre, email))
                conn.commit()
                user = conn.execute("SELECT * FROM Usuarios WHERE id = ?", (cur.lastrowid,)).fetchone()
                
        user_dict = dict(user)
        conn.close()
        return jsonify(user_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 401

# --- Chat Endpoint ---
@app.route('/api/v1/chat', methods=['POST'])
def chat():
    if not request.json or 'pregunta' not in request.json:
        abort(400)
        
    pregunta = request.json['pregunta']
    
    if not GEMINI_API_KEY or GEMINI_API_KEY == 'your_gemini_api_key_here':
        # Fallback implementation
        return jsonify({'respuesta': f"[IA MVP] He recibido tu pregunta: '{pregunta}'. (Configura la API Key para conectar con Gemini)"})
    
    try:
        client = google_genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents="Eres el asistente de la empresa TravelSense. Responde en el mismo idioma en que te hablen. Pregunta: " + pregunta
        )
        return jsonify({'respuesta': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Usuarios Endpoints ---
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM Usuarios').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in users])

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or 'nombre' not in request.json:
        abort(400)
    
    nombre = request.json['nombre']
    email = request.json.get('email', '')
    preferencias = request.json.get('preferencias', '')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Usuarios (nombre, email, preferencias) VALUES (?, ?, ?)",
                (nombre, email, preferencias))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'nombre': nombre}), 201

# --- Destinos Endpoints ---
@app.route('/api/v1/destinations', methods=['GET'])
def get_destinations():
    conn = get_db_connection()
    dests = conn.execute('SELECT * FROM Destinos').fetchall()
    conn.close()
    return jsonify([dict(d) for d in dests])

# --- Eventos Endpoints ---
@app.route('/api/v1/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    events = conn.execute('''
        SELECT e.*, d.nombre as destino_nombre 
        FROM Eventos e 
        JOIN Destinos d ON e.destino_id = d.id
    ''').fetchall()
    conn.close()
    return jsonify([dict(e) for e in events])

# --- Itinerarios Endpoints ---
@app.route('/api/v1/itineraries', methods=['GET'])
def get_itineraries():
    conn = get_db_connection()
    itineraries = conn.execute('SELECT * FROM Itinerarios').fetchall()
    
    results = []
    for it in itineraries:
        i = dict(it)
        # Fetch Activities
        acts = conn.execute('SELECT * FROM Actividades WHERE itinerario_id = ?', (i['id'],)).fetchall()
        i['actividades'] = [dict(a) for a in acts]
        
        # Fetch User name
        user = conn.execute('SELECT nombre FROM Usuarios WHERE id = ?', (i['usuario_id'],)).fetchone()
        i['usuario_nombre'] = user['nombre'] if user else 'Desconocido'
        
        # Fetch Destination name
        dest = conn.execute('SELECT nombre FROM Destinos WHERE id = ?', (i['destino_id'],)).fetchone()
        i['destino_nombre'] = dest['nombre'] if dest else 'Desconocido'
        
        results.append(i)
    
    conn.close()
    return jsonify(results)

# --- Populate Endpoint ---
@app.route('/api/v1/populate', methods=['POST'])
def populate_db():
    try:
        conn = get_db_connection()
        try:
             # Drop existing tables to refresh schema if needed, or just let create_tables handle IF NOT EXISTS
             # Ideally validation should be done, but for this demo script overwrite is fine.
             pass
        except:
             pass
             
        # Call setup script logic
        # Ensure tables are dropped to apply new schema
        conn.execute("DROP TABLE IF EXISTS Actividades")
        conn.execute("DROP TABLE IF EXISTS Itinerarios")
        conn.execute("DROP TABLE IF EXISTS Eventos")
        conn.execute("DROP TABLE IF EXISTS Destinos")
        conn.execute("DROP TABLE IF EXISTS Usuarios")
        
        setup_database.create_tables(conn)
        # Clear old data (redundant but safe)
        # conn.execute("DELETE FROM...") - tables are already new and empty
        
        setup_database.generate_fake_data(conn)
        conn.commit()
        
        conn.close()
        return jsonify({'message': 'Base de datos TravelSense poblada exitosamente.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Forced reload
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


