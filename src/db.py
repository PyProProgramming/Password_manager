# Imports
import os
import sqlite3

# Creating the database file if not already created
if not os.path.exists("data/data.db"):
    with open("data/data.db", "w") as file:
        pass

# Connecting to the database
conn = sqlite3.connect("data/data.db")
# Getting the cursor object
cursor = conn.cursor()

# Creating the table if it already hasn't been made
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
