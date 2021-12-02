import os
import sqlite3

db_name = 'MY.db'
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
        cursor.execute(sql, ('root', 'root'))
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
            cursor.execute("SELECT name, password FROM MY WHERE  name = ? and password = ?", (username, password))
            row1 = cursor.fetchone()
            string = str(row1)
            cursor.execute("SELECT name FROM MY")
            row = cursor.fetchall()
            print(row)
            if string == username:
                print("There is already a user with this name!")
            else:

                udv = "y"
                if string != '' or string == 'root':
                    cursor.execute(sql, (username, password))
                    connection.commit()

                cursor.execute("SELECT name, password FROM MY WHERE  name = ? and password = ?",
                               (username, password))
                row = cursor.fetchone()
                print('Given datas:\nUsername:  ' + row[0] + ' \nPassword: ', row[1])
                break
        else:
            print("Passwords do not match!")

if udv == "y" or udv == "Y":
    while True:
        print("Please log in.")
        login1 = input("Login:")
        login2 = input("Password:")
        uname = ''
        passwd = ''
        row = str(cursor.execute("SELECT name, password FROM MY WHERE name = ? and password = ?", (login1, login2)))
        row1 = cursor.fetchone()
        string1 = str(row1[0])
        string2 = str(row1[1])
        if string1 == login1 and string2 == login2:
            print("Welcome")
            break
        else:
            print("Wrong username or password!")
    while True:
        decision = input("What would you like to do?\nA|Write out users\nB|Use calculator\nC|Exit\n")
        if decision == 'A' or decision == 'a':
            cursor.execute("SELECT name FROM MY")
            row = cursor.fetchall()
            print(row)
        if decision == 'B' or decision == 'b':
            print("Let me calculate for you!")
            print("Give me two numbers, and one operator.")
            num1 = int(input("1. Number:"))
            num2 = int(input("2. Number:"))
            sign = input("Operator(+|-|/|*):")
            v = 0
            if sign == '+':
                v = num1 + num2
            elif sign == '-':
                v = num1 - num2
            elif sign == '*':
                v = num1 * num2
            elif sign == '/':
                v = num1 / num2

            print(str(num1) + ' ' + sign + ' ' + str(num2) + ' = ' + str(v))
        if decision == 'C' or decision == 'c':
            print("Good bye!")
            break

else:
    print("Incorrect username or password.")
