from flask import Flask

from flask import Blueprint

app = Blueprint('app', __name__)

app = Flask(__name__)


@app.route('/')
def welcome():
    print("Welcome...")
    udv = input("Do you have an acount? y/n: ")
    if udv == "n":
        while True:
            username = input("Enter a username:")
            password = input("Enter a password:")
            password1 = input("Confirm password:")
            if password == password1:
                file = open(username + ".txt", "w")
                file.write(username + ":" + password)
                file.close()
                udv = "y"
                break
            print("Passwords do NOT match!")

    if udv == "y":
        while True:
            login1 = input("Login:")
            login2 = input("Password:")
            file = open(login1 + ".txt", "r")
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome")
                break
            print("Incorrect username or password.")


