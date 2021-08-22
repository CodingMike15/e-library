from db import get_db

def insert_book(name, author):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(Name, Author) VALUES (?, ?)"
    cursor.execute(statement, [name, author])
    db.commit()
    return True

def update_book(id, name, author):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE books SET Name = ?, Author = ? WHERE ID = ?"
    cursor.execute(statement, [name, author, id])
    db.commit()
    return True

def delete_book(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM books WHERE ID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, Name, Author FROM books WHERE ID = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_books():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, Name, Author FROM books"
    cursor.execute(query)
    return cursor.fetchall()

def get_by_name(name):
    db = get_db()
    cursor = db.cursor()
    statement = 'SELECT ID, Name, Author FROM books WHERE Name = ?'
    cursor.execute(statement, [name])
    return cursor.fetchall()

def get_by_author(author):
    db = get_db()
    cursor = db.cursor()
    statement = 'SELECT ID, Name, Author FROM books WHERE Author = ?'
    cursor.execute(statement, [author])
    return cursor.fetchall()