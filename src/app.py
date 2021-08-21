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

with open("data/data.json") as file:
    data = json.load(file)

if data != {}:
    print("Please use the master key to acces your passwords: ")
    key = input("Enter your master key : ")

    if data["key"] == hash_string(key):
        print("ur inside!")
    else:
        print("Wrong key try again!")

else:
    print("Please set a master key to access your passwords: ") 
    key = input("Enter your master key : ")

    data["key"] = hash_string(key)
    
    with open("data/data.json", "w") as file:
        json.dump(data, file)

    