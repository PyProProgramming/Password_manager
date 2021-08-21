import sqlite3
import os
import hashlib
import string
import json


if not os.path.exists("data/data.db"):
    with open("data/data.db", "w") as file:
        pass

conn = sqlite3.connect("data/data.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS everything(
    password text, 
    app_url text, 
    app_name text, 
    email text, 
    username text
)""")

# Function to add a password
def add_to_db(username, email, password, app_url, app_name):
    cursor.execute("INSERT INTO everything(password, app_url, app_name, email, username) VALUES (?, ?, ?, ?, ?)",
    (password, app_url, app_name, email, username))
    conn.commit()

# Function to list all password
def list_all():
    cursor.execute("SELECT * FROM everything")
    return cursor.fetchall()

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
        ))

    site_name = input('enter the site/apps name whose password you are looking for : \n')    

    names = []
    for i in list_of_passwords:
        names.append(i.app_name)
    
    if site_name not in names:
        print("Sorry but you haven't stored a password for this site")
    else:
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


def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


def encrypt(text, key):
    """
    This function implements Cesar encryption to encrypt text
    This function encrypts text
    :param key:
    :type text: str
    """
    # make variable to store cyphered text
    encrypted_text = ""
    # loop through each element in text
    for i in text:
        # if its a letter shift its value
        try:
            # get index of i, shift it, get its mod 26, then find
            # corresponding value and concatenate it to encrypted text
            encrypted_text += letters[(letters.index(i) + key) % len(letters)]
        # other vise don't cipher it
        except ValueError:
            encrypted_text += i
    # finally, return ciphered text
    return encrypted_text


def decrypt(text, key):
    """
    This function is the inverse of the encrypt function. It decrypts
    text using the key that was used to encrypt it.
    :param text: Text to decrypt
    :param key: key that was used to encrypt text
    :return: decrypted text
    """
    decrypted_text = ""
    for i in text:
        try:
            decrypted_text += letters[letters.index(i) - key % len(letters)]
        except ValueError:
            decrypted_text += i
    return decrypted_text


letters = string.ascii_letters
# print(letters)
# print(" ".lower() == " ")
# print("a" < "A")


# print(encrypt("hello", 2))
# print(decrypt(encrypt("Hello! My name is Ishan Kashyap", 5), 5))


# author : snehashish laskar
# date : 20-08-2021
# time : 19:38

# THIS IS A PASSWORD MANAGER TO STORE AND MANAGE PASSWORDS
# IT USES SQLITE DATABSE FOR STORING PASSWORDS WHICH CAN BE 
# STORED IN THE FORMS OF FILES LOCALLY ANYWHERE. 
# IT HAS A BASIC CLI MENU FOR USAGE

with open("data/data.json") as file:
    data = json.load(file)

def print_menu():
    print("---------------MENU---------------")
    print("[a] for adding passwords to database")
    print("[s] for getting passwords from the database")
    print("[q] for quiting the application ")
    print("[h] for listing out the menu ")
    print("---------------MENU---------------")

def run_application():
    commands = {
        "a":add_from_user,
        "s":list_for_user,
        "q":exit,
        "h":print_menu
    }
    print_menu()
    while True:
        
        inp = input("$ ")
        
        for i in commands:
            if i == inp:
                func = commands[i]
                func()

if data != {}:
    print("Please use the master key to acces your passwords: ")
    key = input("Enter your master key : ")

    if data["key"] == hash_string(key):
        run_application()
    else:
        print("Wrong key try again!")

else:
    print("Please set a master key to access your passwords: ") 
    key = input("Enter your master key : ")

    data["key"] = hash_string(key)
    
    with open("data/data.json", "w") as file:
        json.dump(data, file)

    