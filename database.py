import sqlite3

DB_NAME = 'travelsense.db'

def get_db_connection():
    """Establishes a connection to the database and sets the row factory."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def query_db(query, args=(), one=False):
    """Executes a query and returns the results."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    """Executes a modification query (INSERT, UPDATE, DELETE) and returns the last row id."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    last_row_id = cur.lastrowid
    conn.close()
    return last_row_id
