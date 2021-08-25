# Author : Snehashish Laskar
# Date : 20-08-2021
# Time : 19:38

# Imports
from db import *
from encryption import *


# Functions to ask the user for the details of the password before storing it into the database
def add_from_user():
    email = input("Enter the email address for this site: \n")
    username = input("Enter the username will use for the site: \n")
    app_name = input("enter the name of the site/app the password is for: \n")
    app_url = input("Enter the url for the site: \n")

    password = input("Enter the password you have used:  \n")
    # print(f"The Encrypted password is: {encrypt(password, key=10)}")

    add_to_db(username, email, encrypt(password, key=10), app_url, app_name)


# A class Password to represent every password
class Password:
    """
    Each password will have:
    -> The username used for the signup 
    -> The email address used for the sign in
    -> The password
    -> The app or site's Url
    -> The app of site's name
    """

    def __init__(self, username, email, password, app_url, app_name):
        self.username = username
        self.email = email
        self.password = decrypt(password, key=10)
        self.app_url = app_url
        self.app_name = app_name

    # Function to return the data
    def form_data(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "app_name": self.app_name,
            "app_url": self.app_url,
        }


# Function to look through the database for passwords
def list_for_user():
    list_of_passwords = []
    # Reading the table (in hasher.py) and forming a list of passwords objects
    for i in list_all():
        list_of_passwords.append(Password(
            username=i[4],
            email=i[3],
            password=i[0],
            app_url=i[1],
            app_name=i[2]
        ))

    # getting the user input for which site's passwords they are looking for
    site_name = input('enter the site/apps name whose password you are looking for : \n')

    # Getting all the names of sites in the database
    names = []
    for i in list_of_passwords:
        names.append(i.app_name)

    # Checking if the site is there in the database or not
    if site_name not in names:
        # If not then telling the user
        print("Sorry but you haven't stored a password for this site")
    else:
        # Otherwise printing out the details about the password
        for i in list_of_passwords:
            if site_name == i.app_name:
                print("\n-------DETAILS-------")
                print(f"App Name : {i.app_name}")
                print(f"App Url : {i.app_url}")
                print(f"email used : {i.email}")
                print(f"username : {i.username}")
                print(f"password: {i.password}")
            else:
                pass
