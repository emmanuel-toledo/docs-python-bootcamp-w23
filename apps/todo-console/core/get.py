import json

from db.db_context import select_all, select_by_id
from utils.parse_db_response import parse_todo_to_json_array, parse_todo_to_json

def select_tasks():
    tasks = select_all() # Consulta a la BD
    json_tasks = parse_todo_to_json_array(tasks) # Convertimos a un arreglo JSON
    print(json.dumps(json_tasks, indent = 4)) # Imprimimos el resultado (JSON de línea anterior)

def select_task():
    id = input("Escribe el identificador del registro que deseas consultar: ")
    task = select_by_id(id) # Consulta a la BD
    if task == None:
        print(f"ERROR: El registro con el id '{id}' no existe")
        return None
    json_task = parse_todo_to_json(task) # Convertimos a un objeto JSON
    print(json.dumps(json_task, indent = 4)) # Imprimimos el resultado (JSON de línea anterior)
