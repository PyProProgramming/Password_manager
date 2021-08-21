from db import *
from encryption import *

def add_from_user():

    email = input("Enter the email adress for this site: \n")
    username = input("Enter the username will use for the site: \n")
    app_name = input("enter the name of the site/app the password is for: \n ")
    app_url = input("Enter the url for the site: \n")

    password = input("Enter a simple password you can remember: ")
    print(f"The Encrypted password is: {encrypt(password, key=10)}")

    add_to_db(username, email, encrypt(password, key=10), app_url, app_name)

class Password: 

    def __init__(self, username, email, password , app_url, app_name):
        self.username = username
        self.email = email
        self.password = password
        self.app_url = app_url
        self.app_name = app_name

    def form_data(self):
        return {
            "username": self.username,
            "password": self.password,
            "email":self.email,
            "app_name": self.app_name,
            "app_url":self.app_url,
        }

def list_for_user():
    list_of_passwords = []

    for i in list_all():
        list_of_passwords.append(Password(
            username=i[4],
            email=i[3],
            password=i[0],
            app_url = i[1],
            app_name=i[2]
        ).form_data())

    print(list_of_passwords)

list_for_user()
