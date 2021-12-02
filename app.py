import os
import sqlite3
import sqlite3 as sl

db_name = 'MY.db'
db_exists = not os.path.exists(db_name)
con = sl.connect('./MY.db')
connection = sqlite3.connect(db_name)
cur = con.cursor()
sql = "INSERT INTO MY (name, password) VALUES(?, ?)"
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
udv = input("Do you have an account? y/n: ")
if udv == "n":
    while True:
        username = input("Enter a username:")
        password = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            var = cur.execute(sql, (username, password))
            udv = "y"
            cur.execute("SELECT name, password FROM MY WHERE  name = ? and password = ?", (username, password))
            row = cur.fetchall()
            print('Given datas:\nUsername: ? \nPassword: ?', row[0], row[1])
            break
        print("Passwords do NOT match!")

if udv == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        uname = ''
        passwd = ''
        cur.execute("SELECT name, password FROM MY")
        row = cur.fetchall()
        if row[0] == uname and row[1] == passwd:
            print(login1, login2)
            print("Welcome")
        decision = input("What would you like to do?\nA|Write out users\nB|Use calculator\n")
        if decision == 'A' or decision == 'a':
            cur.execute("SELECT * FROM MY")
            row = cur.fetchall()
            for x in row:
                print(x)

        break

else:
    print("Incorrect username or password.")
