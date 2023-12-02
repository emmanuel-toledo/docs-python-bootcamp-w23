import sqlite3

connection = sqlite3.connect("./db/todo.sqlite3")
cursor = connection.cursor()

def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status INTEGER DEFAULT 1,
            created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_on TIMESTAMP
        )
        """)
    connection.commit()

def insert(todo):
    cursor.execute("""INSERT INTO todo (name, description) VALUES (:name, :description)""", (todo))
    connection.commit()
    return cursor.lastrowid

def delete(id):
    cursor.execute("""DELETE FROM todo WHERE id = ?""", (id,))
    connection.commit()

def update(todo):
    cursor.execute("""UPDATE todo 
                    SET name = :name, 
                    description = :description, 
                    status = :status 
                    WHERE id = :id""", (todo))
    connection.commit()

def complete(id):
    cursor.execute("""UPDATE todo 
                    SET status = 0,
                    completed_on = CURRENT_TIMESTAMP
                    WHERE id = :id""", (id,))
    connection.commit()

def reopen(id):
    cursor.execute("""UPDATE todo
                    SET status = 1,
                    completed_on = NULL
                    WHERE id = :id""", (id,))
    connection.commit()

def select_all():
    # STRFTIME sirve para dar formato a una columna de tipo TIMESTAMP
    cursor.execute("SELECT id, name, description, status, STRFTIME('%d/%m/%Y %H:%M:%S', created_on) AS created_on, STRFTIME('%d/%m/%Y %H:%M:%S', completed_on) AS completed_on FROM todo")
    return cursor.fetchall()

def select_by_id(id):
    # Se coloca (id,) ya que la función execute recibe una tupla de valores, y le damos una tupla de un solo valor.
    cursor.execute("""SELECT 
                   id, 
                   name, 
                   description, 
                   status, 
                   STRFTIME('%d/%m/%Y %H:%M:%S', created_on) AS created_on, 
                   STRFTIME('%d/%m/%Y %H:%M:%S', completed_on) AS completed_on 
                   FROM todo WHERE id = ?""", (id,))
    return cursor.fetchone()