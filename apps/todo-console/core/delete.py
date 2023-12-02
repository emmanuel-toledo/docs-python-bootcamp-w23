from db.db_context import delete

def delete_task():
    id = input("Escribe el identificador del registro que deseas eliminar: ")
    delete(id)
    print(f"El registro con el id '{id}' se eliminó correctamente")
