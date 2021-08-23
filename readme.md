# E-Library
---
E-Library is a web app to manage a data base were I keep track of the ebooks I have. With this web app you can see all the books,find a book by the id, find a book by the name and author, insert a book into the data base, deleta a book and update a book.

### Prerequisites
---
- Python3
- flask
- mariadb

### Installation
---
To clone the repostitory you need follow this steps:

1. Open the terminal.
2. Change to the directory where you want to clon the directory.
3. Copy the following line into the terminal: `https://github.com/CodingMike15/e-library.git`.
4. Press ENTER to create the local clon.

### Usage
---
You need to have a user and database in MariaDB, and in db.py change in the get_db function the user variable with the your user, the password variable with the password of your user and change the database variable with your database name.

1. Run the main.py file in the src directory
2. It will create a sever in localhost:5000
If you want to change the port change `app.run(port='<port>')`