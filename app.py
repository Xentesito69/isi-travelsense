from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import sqlite3
import database
import setup_database

app = Flask(__name__)
CORS(app)
DB_NAME = 'travelsense.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

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
    app.run(debug=True)

