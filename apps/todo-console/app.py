from db.db_context import create_tables

from core.create import insert_task
from core.get import select_tasks, select_task
from core.delete import delete_task
from core.update import update_task, complete_task, reopen_task

if __name__ == "__main__":
    create_tables()
    exit_app = False
    while(exit_app == False):
        print("""Selecciona la opción que deseas:
              1) Obtener todas las tareas.
              2) Obtener un registro por su identificador.
              3) Crear una nueva tarea.
              4) Eliminar una tarea.
              5) Actualizar tarea.
              6) Completar una tarea.
              7) Re-abrir una tarea.
              8) Salir.
              """)
        selected_option = int(input())
        if selected_option == 1:
            select_tasks()
        elif selected_option == 2:
            select_task()
        elif selected_option == 3:
            insert_task()
        elif selected_option == 4:
            delete_task()
        elif selected_option == 5:
            update_task()
        elif selected_option == 6:
            complete_task()
        elif selected_option == 7:
            reopen_task()
        elif selected_option == 8:
            exit_app = True
            print("Gracias por usar ToDo app!! :D")
        else:
            print("Selecciona una opción válida")
        print("\n\n\n")
        pass

