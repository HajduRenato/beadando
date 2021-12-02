import sqlite3
import sqlite3 as sl

con = sl.connect('../my-test.db')


def __init__(self, db_name):
    self.db_name = db_name  # database name
    self.conn = None  # connection


def check_database(self):
    """ Check if the database exists or not """
    try:
        print(f'Checking if {self.db_name} exists or not...')
        self.conn = sqlite3.connect(self.db_name, uri=True)
        print(f'Database exists. Succesfully connected to {self.db_name}')
    except sqlite3.OperationalError as err:
        print('Database does not exist')
        print(err)


with con:
    con.execute("""
        CREATE TABLE DB (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)
    sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
    data = [
        (1, 'Alice', 21),
        (2, 'Bob', 22),
        (3, 'Chris', 23)
    ]
