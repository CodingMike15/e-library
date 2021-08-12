from flask import Flask, jsonify, request
import book_controller
from db import create_tables

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_books():
    books = book_controller.get_books()
    return jsonify(books)

@app.route('/book/<id>', methods=['GET'])
def get_book_by_id(id):
    book = book_controller.get_by_id(id)
    return jsonify(book)

@app.route('/book', methods=['POST'])
def insert_book():
    book_details = request.get_json()
    name = book_details['name']
    author = book_details['author']
    result = book_controller.insert_book(name, author)
    return jsonify(result)

@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    result = book_controller.delete_book(id)
    return jsonify(result)

@app.route('/book', methods=['PUT'])
def update_book():
    book_details = request.get_json()
    id = book_details['id']
    name = book_details['name']
    author = book_details['author']
    result = book_controller.update_book(id, name, author)
    return jsonify(result)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)