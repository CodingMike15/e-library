import secrets
import mariadb
from secrets import user, password

def get_db():
    conn = mariadb.connect( 
        user= user, 
        password= password, 
        host="localhost", 
        database="elibrary"
    )
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS books(
                ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Name varchar(255) NOT NULL,
                Author varchar(255) NOT NULL
            );
            """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)