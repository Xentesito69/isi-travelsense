import sqlite3
import setup_database
import traceback

DB_NAME = 'travelsense.db'

def debug_populate():
    print("Iniciando depuración...")
    try:
        conn = sqlite3.connect(DB_NAME)
        print("Conexión establecida.")
        
        setup_database.create_tables(conn)
        print("Tablas verificadas.")
        
        print("Generando datos falsos...")
        setup_database.generate_fake_data(conn)
        print("Datos generados correctamente.")
        
        conn.close()
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    debug_populate()
