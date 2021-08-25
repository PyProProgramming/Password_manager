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

# Opening the json file to be able to access the key
with open("data/data.json") as file:
    data = json.load(file)

# Function to print the menu
def print_menu():
    print("---------------MENU---------------")
    print("[add] for adding passwords to database")
    print("[search] for getting passwords from the database")
    print("[exit] for quiting the application ")
    print("[help] for listing out the menu ")
    print("---------------MENU---------------")

# The Core of the appliation
def run_application():
    # A list of commands and the functions to react to the commands
    commands = {
        "add":add_from_user,
        "search":list_for_user,
        "exit":exit,
        "help":print_menu
    }
    # Main core
    # Printing the menu on startup
    print_menu()
    # Running a forever loop
    while True:
        # getting the user input
        inp = input("$ ")
        # running through the commands
        for i in commands:
            # Checking if the input is a valid command
            if i == inp:
                # if yes then calling the response function
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

