import json
from utils.parse_db_response import parse_todo_to_json
from db.db_context import insert, select_by_id

def insert_task():
    # Obtenemos los datos de la tarea
    name = input("Escribe el nombre de la tarea: ")
    description = input("Escribe la descripción de la tarea: ")
    # Registramos en la BD y obtenemos el Id
    id = insert(
        { 
            "name": name, 
            "description": description 
        }
    )
    # Consultamos el registro con el Id recién registrado
    task = select_by_id(id)
    # Convertimos a un objeto JSON e imprimimos
    json_task = parse_todo_to_json(task)
    print(json.dumps(json_task, indent = 4))
    print("Se registro con éxito la tarea :D")
    pass
