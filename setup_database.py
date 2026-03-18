import sqlite3
import random
import datetime

DB_NAME = 'travelsense.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    # Same table creation logic
    sql_create_usuarios = """
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE,
        preferencias TEXT,
        historial_viajes TEXT,
        pais TEXT
    );"""
    sql_create_destinos = """
    CREATE TABLE IF NOT EXISTS Destinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        clima_tipico TEXT,
        pais TEXT,
        region TEXT
    );"""
    sql_create_itinerarios = """
    CREATE TABLE IF NOT EXISTS Itinerarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        destino_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        resumen_narrativo TEXT,
        clima_actual TEXT,
        FOREIGN KEY (usuario_id) REFERENCES Usuarios (id),
        FOREIGN KEY (destino_id) REFERENCES Destinos (id)
    );"""
    sql_create_actividades = """
    CREATE TABLE IF NOT EXISTS Actividades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        itinerario_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        tipo TEXT,
        hora TEXT,
        justificacion_ia TEXT,
        FOREIGN KEY (itinerario_id) REFERENCES Itinerarios (id)
    );"""
    sql_create_eventos = """
    CREATE TABLE IF NOT EXISTS Eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        destino_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        tipo TEXT, 
        fecha TEXT,
        precio TEXT,
        FOREIGN KEY (destino_id) REFERENCES Destinos (id)
    );"""

    try:
        c = conn.cursor()
        c.execute(sql_create_usuarios)
        c.execute(sql_create_destinos)
        c.execute(sql_create_itinerarios)
        c.execute(sql_create_actividades)
        c.execute(sql_create_eventos)
        print("Tablas creadas/verificadas.")
    except sqlite3.Error as e:
        print(f"Error creando tablas: {e}")

def generate_fake_data(conn):
    c = conn.cursor()

    # --- DATOS PROBATORIOS (Data Pools) ---
    NOMBRES = [
        ('Javier', 'España'), ('Mariam', 'España'), ('Noelia', 'España'), ('Vicente', 'España'), 
        ('Felix', 'España'), ('Ana', 'España'), ('Carlos', 'España'), ('Elena', 'España'),
        ('Lucía', 'España'), ('Pablo', 'España'), ('Marta', 'España'), ('Diego', 'España'),
        ('Sergio', 'España'), ('Raquel', 'España'), ('Jorge', 'España'), ('Beatriz', 'España'),
        ('Pierre', 'Francia'), ('Marie', 'Francia'), ('Jean', 'Francia'), ('Sophie', 'Francia'),
        ('Hans', 'Alemania'), ('Greta', 'Alemania'), ('Klaus', 'Alemania'), ('Ursula', 'Alemania'),
        ('Yuki', 'Japón'), ('Kenji', 'Japón'), ('Haruto', 'Japón'), ('Akiko', 'Japón'),
        ('Wei', 'China'), ('Li', 'China'), ('Chen', 'China'), ('Mei', 'China'),
        ('Fatima', 'Marruecos'), ('Ahmed', 'Egipto'), ('Omar', 'EAU'), ('Layla', 'Jordania'),
        ('John', 'USA'), ('Sarah', 'USA'), ('Michael', 'USA'), ('Emma', 'USA'),
        ('James', 'USA'), ('Emily', 'USA'), ('Robert', 'USA'), ('Jessica', 'USA'),
        ('David', 'UK'), ('Laura', 'Italia'), ('Marco', 'Italia'), ('Giulia', 'Italia'),
        ('Luca', 'Italia'), ('Sofia', 'Italia'), ('Alessandro', 'Italia'), ('Francesca', 'Italia'),
        ('Lars', 'Suecia'), ('Ingrid', 'Noruega'), ('Sven', 'Dinamarca'), ('Astrid', 'Suecia'),
        ('Mateo', 'Argentina'), ('Valentina', 'Argentina'), ('Thiago', 'Brasil'), ('Camila', 'Chile'),
        ('Alejandro', 'México'), ('Sofia', 'México'), ('Diego', 'Colombia'), ('Isabella', 'Colombia')
    ]
    APELLIDOS = [
        'García', 'López', 'Martínez', 'Sánchez', 'Rodríguez', 'Pérez', 'Gómez', 'Smith', 'Johnson', 
        'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Müller', 'Schmidt', 'Dubois', 'Leroy', 
        'Tanaka', 'Suzuki', 'Wang', 'Li', 'Khan', 'Ali', 'Rossi', 'Bianchi', 'Colombo', 'Ricci',
        'Silva', 'Santos', 'Oliveira', 'Costa', 'Pereira', 'Fernández', 'González', 'Hernández'
    ]
    
    from datos_viaje import DESTINOS_POOL

    PREFS_POOL = [
        'Gastronomía', 'Deporte', 'Cultura', 'Relax', 'Naturaleza', 'Historia', 'Aventura', 
        'Fotografía', 'Compras', 'Lujo', 'Mochilero', 'Arte', 'Vino', 'Tecnología', 
        'Espiritualidad', 'Vida Nocturna', 'Arquitectura', 'Playa'
    ]
    
    CLIMA_POOL = ['Soleado', 'Lluvioso', 'Nublado', 'Ventoso', 'Tormenta', 'Nieve', 'Niebla']
    
    # --- 1. Generar Usuarios Random ---
    num_users = 100 # Exact user request
    current_users = []
    
    print(f"Generando {num_users} usuarios...")
    used_emails = set()
    
    for _ in range(num_users):
        nombre_tuple = random.choice(NOMBRES)
        nombre = nombre_tuple[0]
        pais = nombre_tuple[1]
        apellido = random.choice(APELLIDOS)
        
        full_name = f"{nombre} {apellido}"
        
        # Ensure unique email
        base_email = f"{nombre.lower()}.{apellido.lower()}"
        counter = 1
        email = f"{base_email}@travelsense.com"
        while email in used_emails:
            email = f"{base_email}{counter}@travelsense.com"
            counter += 1
        used_emails.add(email)
        
        # 2 to 4 random preferences
        num_prefs = random.randint(2, 4)
        prefs = random.sample(PREFS_POOL, num_prefs)
        prefs_str = ", ".join(prefs)
        
        c.execute("INSERT INTO Usuarios (nombre, email, preferencias, pais) VALUES (?, ?, ?, ?)",
                  (full_name, email, prefs_str, pais))
        usuario_id = c.lastrowid
        current_users.append((usuario_id, full_name, prefs))

    # --- 2. Insertar Destinos (Todos) ---
    print(f"Insertando {len(DESTINOS_POOL)} destinos globales...")
    current_dests = []
    for city, desc, weather, country, region in DESTINOS_POOL:
        c.execute("INSERT INTO Destinos (nombre, descripcion, clima_tipico, pais, region) VALUES (?, ?, ?, ?, ?)",
                  (city, desc, weather, country, region))
        current_dests.append((c.lastrowid, city, weather))

    # --- 3. Generar Itinerarios y Actividades ---
    num_itinerarios = 100 # Exact user request
    print(f"Generando {num_itinerarios} itinerarios inteligentes...")
    
    NARRATIVE_TEMPLATES = [
        "Hola {u}, he preparado un viaje a {d} basado en tu gusto por [{p}]. Aprovechando que estará {c}, disfrutarás al máximo.",
        "¡{u}! Tu aventura en {d} está lista. He priorizado actividades de [{p}] dado el clima {c} previsto.",
        "Para ti, {u}: Un recorrido exclusivo por {d}. La selección de [{p}] es perfecta para estos días de clima {c}.",
        "Destino: {d}. Viajero: {u}. Enfoque: [{p}]. Pronóstico: {c}. El plan perfecto te espera.",
        "Basado en tus intereses en [{p}], este itinerario en {d} te sorprenderá. Prepárate para un clima {c}."
    ]

    ACTIVIDAD_TEMPLATES = {
        'Mañana': [
            ('Visita guiada: Lo mejor de {d}', 'Coincide con tus intereses culturales.'),
            ('Ruta de senderismo panorámica', 'Perfecto para disfrutar de la naturaleza.'),
            ('Desayuno en café local histórico', 'Para empezar el día con gastronomía local.'),
            ('Tour de arquitectura moderna', 'Basado en tu interés por el diseño.'),
            ('Clase de yoga al amanecer', 'Para tu preferencia de relax y espiritualidad.')
        ],
        'Tarde': [
            ('Tiempo libre en centro de {d}', 'Disfruta del ambiente a tu ritmo.'),
            ('Visita a museo de arte contemporáneo', 'Recomendado por tu perfil artístico.'),
            ('Compras en distrito de moda', 'Basado en tu gusto por el shopping.'),
            ('Cata de vinos regionales', 'Experiencia gastronómica premium.'),
            ('Aventura en kayak/bici', 'Actividad deportiva recomendada.')
        ],
        'Noche': [
            ('Cena degustación en restaurante estrella', 'Lo mejor de la gastronomía local.'),
            ('Espectáculo nocturno tradicional', 'Inmersión cultural total.'),
            ('Paseo bajo las estrellas', 'Momento de relax al final del día.'),
            ('Ruta de bares y pubs', 'Para experimentar la vida nocturna.'),
            ('Fotografía nocturna de monumentos', 'Captura la ciudad iluminada.')
        ]
    }

    for _ in range(num_itinerarios):
        u_id, u_name, u_prefs = random.choice(current_users)
        d_id, d_name, d_weather = random.choice(current_dests)
        
        # Random date in future
        days_offset = random.randint(1, 60)
        date = (datetime.date.today() + datetime.timedelta(days=days_offset)).strftime("%Y-%m-%d")
        
        # Real-time weather simulation (variation of typical)
        clima_actual = random.choice([d_weather, random.choice(CLIMA_POOL)])
        
        # Narrative
        template = random.choice(NARRATIVE_TEMPLATES)
        narrative = template.format(u=u_name.split()[0], d=d_name, p=", ".join(u_prefs[:2]), c=clima_actual.lower())
        
        c.execute("INSERT INTO Itinerarios (usuario_id, destino_id, fecha, resumen_narrativo, clima_actual) VALUES (?, ?, ?, ?, ?)",
                  (u_id, d_id, date, narrative, clima_actual))
        itinerario_id = c.lastrowid
        
        # Activities (3 per itinerary)
        horas = ['09:30', '10:00', '11:00', '13:00', '14:30', '16:00', '17:30', '19:00', '21:00']
        selected_horas = sorted(random.sample(horas, 3))
        
        moments = ['Mañana', 'Tarde', 'Noche']
        
        for i, hora in enumerate(selected_horas):
            moment = moments[i]
            act_name_tpl, act_just = random.choice(ACTIVIDAD_TEMPLATES[moment])
            act_name = act_name_tpl.format(d=d_name)
            
            c.execute("INSERT INTO Actividades (itinerario_id, nombre, tipo, hora, justificacion_ia) VALUES (?, ?, ?, ?, ?)",
                      (itinerario_id, act_name, 'General', hora, act_just))
            
    conn.commit()
    
    # --- 4. Generar Eventos Locales ---
    print("Generando eventos locales...")
    
    from datos_viaje import generate_events_for_destination

    for d_id, d_name, _ in current_dests:
        events_list = generate_events_for_destination(d_name)
            
        for ev_name, ev_type, ev_price in events_list:
             # Random date
            days_offset = random.randint(5, 90)
            ev_date = (datetime.date.today() + datetime.timedelta(days=days_offset)).strftime("%Y-%m-%d")
            
            c.execute("INSERT INTO Eventos (destino_id, nombre, tipo, fecha, precio) VALUES (?, ?, ?, ?, ?)",
                      (d_id, ev_name, ev_type, ev_date, ev_price))

    conn.commit()
    print("Datos (incluyendo eventos) insertados exitosamente.")

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        generate_fake_data(conn)
        conn.close()
    else:
        print("Error: No se pudo conectar a la BD.")

if __name__ == '__main__':
    main()
