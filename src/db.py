import sqlite3

DATABASE_NAME = "books.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                author TEXT NOT NULL
            )
            """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)