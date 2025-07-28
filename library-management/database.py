import sqlite3

def connect_db():
    conn = sqlite3.connect('library.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            type TEXT NOT NULL,
            is_borrowed BOOLEAN NOT NULL DEFAULT 0,
            borrow_count INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def list_available_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE is_borrowed = 0')
    available_items = cursor.fetchall()
    conn.close()
    return available_items

def list_borrowed_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE is_borrowed = 1')
    borrowed_items = cursor.fetchall()
    conn.close()
    return borrowed_items

def most_borrowed_item():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT title, COUNT(*) as borrow_count FROM items WHERE is_borrowed = 1 GROUP BY title ORDER BY borrow_count DESC LIMIT 1')
    most_borrowed = cursor.fetchone()
    conn.close()
    return most_borrowed