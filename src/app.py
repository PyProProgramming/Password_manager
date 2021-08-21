# author : snehashish laskar
# date : 20-08-2021
# time : 19:38

# THIS IS A PASSWORD MANAGER TO STORE AND MANAGE PASSWORDS
# IT USES SQLITE DATABSE FOR STORING PASSWORDS WHICH CAN BE 
# STORED IN THE FORMS OF FILES LOCALLY ANYWHERE. 
# IT HAS A BASIC CLI MENU FOR USAGE

# Imports
from db import *
from hasher import *
import json
from interface import *

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

    