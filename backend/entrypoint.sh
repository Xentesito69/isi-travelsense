#!/bin/sh
set -e

DB_FILE="${DB_PATH:-/app/data/travelsense.db}"
DB_DIR=$(dirname "$DB_FILE")

# Asegurarse de que el directorio del volumen existe
mkdir -p "$DB_DIR"

# Inicializar la base de datos si no existe o está vacía
if [ ! -f "$DB_FILE" ] || [ ! -s "$DB_FILE" ]; then
    echo "[entrypoint] Inicializando base de datos en $DB_FILE ..."
    python -c "
import sqlite3, sys, os
sys.path.insert(0, '/app')
import setup_database
conn = sqlite3.connect('$DB_FILE')
conn.row_factory = sqlite3.Row
setup_database.create_tables(conn)
setup_database.generate_fake_data(conn)
conn.commit()
conn.close()
print('[entrypoint] Base de datos inicializada correctamente.')
"
else
    echo "[entrypoint] Base de datos ya existe, omitiendo inicialización."
fi

# Arrancar gunicorn
exec gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 120 app:app
