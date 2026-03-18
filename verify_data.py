import sqlite3

DB_NAME = 'company_data.db'

def verify():
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        
        tables = ['Customers', 'Categories', 'Products', 'Bills', 'BillItems']
        for table in tables:
            c.execute(f"SELECT COUNT(*) FROM {table}")
            count = c.fetchone()[0]
            print(f"{table}: {count} rows")
            
        c.execute("SELECT * FROM Products LIMIT 1")
        print(f"Sample Product: {c.fetchone()}")

        conn.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify()
