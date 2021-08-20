import sqlite3
import os

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
    print(cursor.fetchall())

list_all()