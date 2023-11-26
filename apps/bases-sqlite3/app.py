import sqlite3
import json
from datetime import datetime

connection = sqlite3.connect("base.sqlite3")
cursor = connection.cursor()

def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL
        ) 
        """)
    # Debemos de hacer un commit para hacer que persevere en la base de datos el cambio.
    connection.commit()
    
def insert_user(name, email):
    cursor.execute("""INSERT INTO users (name, email) VALUES (?, ?)""", (name, email))
    # Debemos de hacer un commit para hacer que persevere en la base de datos el cambio.
    connection.commit()

def insert_user_named_style(user):
    cursor.execute("""INSERT INTO users (name, email) VALUES (:name, :email)""", (user))
    # Debemos de hacer un commit para hacer que persevere en la base de datos el cambio.
    connection.commit()

# Retorna una tupla de los registros de la tabla.
def select_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall() # Retorna una lista de todos los registros.
    # return cursor.fetchmany(10) # Retorna una cierta cantidad de todos los registros.
    # return cursor.fetchone() # Retorna solo el primer registro.

def select_all_user_as_json():
    users = select_all_users()
    json_users = []
    for user in users:
        json_users.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })
    print(json_users)

if __name__ == "__main__":
    create_tables()
    insert_user('Kate Doe', 'kate@test.com')
    insert_user_named_style(
        {
            "name": 'Bob Ross',
            "email": 'bobross@test.com' 
        }
    )
    print(select_all_users())
    select_all_user_as_json()
    # Trabajando con fechas:
    print(datetime.now())

