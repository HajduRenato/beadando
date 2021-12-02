import os
import sqlite3
import sqlite3 as sl

db_name = 'MY.db'
db_exists = not os.path.exists(db_name)
con = sl.connect('./MY.db')
connection = sqlite3.connect(db_name)
cur = con.cursor()
if db_exists:

    with con:
        con.execute("""
            CREATE TABLE MY (
                name TEXT,
                password TEXT
            );
        """)
        print('DB created.')
else:
    print('DB exists.')

print("Welcome...")
udv = input("Do you have an acount? y/n: ")
if udv == "n":
    while True:
        username = input("Enter a username:")
        password = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            var = cur.execute("INSERT INTO MY ( name, password ) VALUES( ?, ?)", (username, password)).rowcount
            udv = "y"
            print('Given datas:\nUsername:'+username+'\nPassword: '+password1)
            break
            print("Passwords do NOT match!")

if udv == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        write = cur.execute('SELECT ?, ? FROM MY', (login1, login2))
        print("Welcome")
        break

else:
    print("Incorrect username or password.")
