import os
import sqlite3
import split

db_name = 'MY.sql'
db_exists = not os.path.exists(db_name)

connection = sqlite3.connect(db_name)
cursor = connection.cursor()
sql = "INSERT INTO MY (name, password) VALUES(?, ?)"
if db_exists:

    with connection:
        connection.execute("""
            CREATE TABLE MY (
                name TEXT,
                password TEXT
            );
        """)
        sql = "INSERT INTO MY (name, password) VALUES(?, ?)"
        data = [
            ('Alice', 'a1'),
            ('Bob', 'b2'),
            ('Chris', 'c3')
        ]
        print('DB created.')
else:
    print('DB exists.')

print("Welcome...")
udv = input("Do you have an account? y/n: ")
if udv == "n" or udv == "N":
    while True:
        username = input("Enter a username:")
        password = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            var = cursor.execute(sql, (username, password))
            udv = "y"
            asd = cursor.execute("SELECT name, password FROM MY WHERE  name = ? and password = ?", (username, password))
            row = cursor.fetchone()
            print('Given datas:\nUsername:  ' + row[0] + ' \nPassword: ', row[1])
            break
        print("Passwords do NOT match!")

if udv == "y" or udv == "Y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        uname = ''
        passwd = ''
        row = str(cursor.execute("SELECT name, password FROM MY"))
        row1 = cursor.fetchall()

        print(login1, login2, row1[0])
        if row[0] == login1 and row[1] == login2:
            print("Welcome")
        decision = input("What would you like to do?\nA|Write out users\nB|Use calculator\n")
        if decision == 'A' or decision == 'a':
            cursor.execute("SELECT name FROM MY")
            row = str(cursor.fetchone())
            for x in row:
                print(x)

        break

else:
    print("Incorrect username or password.")
