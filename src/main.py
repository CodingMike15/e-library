from flask import Flask, jsonify, request, render_template
import book_controller
from db import create_tables, get_db

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_books():
    books = book_controller.get_books()
    return render_template('get_books.html', books=books)

@app.route('/findbookbyid', methods=['GET', 'POST'])
def get_book_by_id():
    if request.method == 'GET':
        return render_template('find_book_by_id.html')

    if request.method == 'POST':
        book_id = request.form['book']
        book = book_controller.get_by_id(book_id)
        return render_template('find_book_by_id.html', book=book)

@app.route('/findbookbyname', methods=['GET', 'POST'])
def get_book_by_name():
    if request.method == 'GET':
        return render_template('find_book_by_name.html')

    if request.method == 'POST':
        book_name = request.form['name']
        book = book_controller.get_by_name(book_name)
        return render_template('find_book_by_name.html', book=book)

@app.route('/insertbook', methods=['GET', 'POST'])
def insert_book():
    if request.method == 'GET':
        return render_template('insert_book.html')

    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        result = book_controller.insert_book(name, author)
        message = 'Book Inserted'
        return render_template('insert_book.html', message=message)

@app.route('/deletebook', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'GET':
        return render_template('delete_book.html')

    if request.method == 'POST':
        book = request.form['book']
        result = book_controller.delete_book(book)
        message = 'Book Deleted'
        return render_template('delete_book.html', message=message)

@app.route('/updatebook', methods=['GET', 'POST'])
def update_book():
    if request.method == 'GET':
        return render_template('update_book.html')

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        author = request.form['author']
        result = book_controller.update_book(id, name, author)
        message = 'Book Updated'
        return render_template('update_book.html', message=message)
        

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)