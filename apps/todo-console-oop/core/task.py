from datetime import datetime
from models.task import Task as _Task
from db.task_context import Task_Context as _Task_Context
from utils.parse import parse_tasks as _parse_tasks, parse_task as _parse_task, parse_to_json as json, parse_to_json_array as json_array

task_context = _Task_Context()

def get():
    return print(json_array(_parse_tasks(task_context.get_all())))

def get_by_id(id):
    task = _Task(id)
    task = task_context.get(task)
    if task == None:
        print("El registro seleccionado no existe")
        return
    return print(json(_parse_task(task)))

def add():
    task = _Task()
    task.set_name(input("Escribe el nombre de la actividad: "))
    task.set_description(input("Escribe la descripción de la actividad: "))
    task.set_created_on(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    id = task_context.add(task)
    return get_by_id(id)

def update():
    id = input("Escribe el identificador del registro que deseas actualizar: ")
    name = input("Escribe el nombre de la tarea: ")
    description = input("Escribe la descripción de la tarea: ")
    status = input("Escribe el estatus de la tarea (1 = activo, 0 = completado): ")
    task = _Task(id, name, description, status)
    if status == "0":
        task.set_completed_on(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    else:
        task.set_completed_on(None)
    task_context.update(task)
    print("Se actualizó el registro correctamente :D")
    return get_by_id(id)

def delete(id):
    task = _Task(id)
    task = task_context.get(task)
    if task == None:
        print("El registro seleccionado no existe")
        return
    task_context.delete(_parse_task(task))
    print("El registro se elimino correctamente")
    pass