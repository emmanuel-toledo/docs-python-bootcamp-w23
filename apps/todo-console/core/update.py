from db.db_context import update, complete, reopen

def update_task():
    # Obtenemos los datos de la tarea
    id = input("Escribe el identificador del registro que deseas actualizar: ")
    name = input("Escribe el nombre de la tarea: ")
    description = input("Escribe la descripción de la tarea: ")
    status = input("Escribe el estatus de la tarea (1 = activo, 0 = completado): ")
    # Actualizamos en la BD
    id = update(
        { 
            "id": id, 
            "status": status, 
            "name": name, 
            "description": description
        }
    )
    print("Se actualizó con éxito la tarea :D")
    pass

def complete_task():
    # Obtenemos los datos de la tarea
    id = input("Escribe el identificador del registro que deseas actualizar: ")
    complete(id)
    print("Se completó con éxito la tarea :D")
    pass

def reopen_task():
    # Obtenemos los datos de la tarea
    id = input("Escribe el identificador del registro que deseas actualizar: ")
    reopen(id)
    print("Se re-abrio con éxito la tarea :D")
    pass
