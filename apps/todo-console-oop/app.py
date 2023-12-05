import core.task as Task_Core

if __name__ == "__main__":
    exit_app = False
    while(exit_app == False):
        selected_option = int(input("""Selecciona la opción que deseas:
              1) Obtener todas las tareas.
              2) Obtener un registro por su identificador.
              3) Crear una nueva tarea.
              4) Eliminar una tarea.
              5) Actualizar tarea.
              6) Salir.
              """))
        if selected_option == 1:
            Task_Core.get()
        elif selected_option == 2:
            Task_Core.get_by_id(
                int(input("Ingresa el id del registro: "))
            )
        elif selected_option == 3:
            Task_Core.add()
        elif selected_option == 4:
            Task_Core.delete(
                int(input("Ingresa el id del registro: "))
            )
        elif selected_option == 5:
            Task_Core.update()
        elif selected_option == 6:
            exit_app = True
            print("Gracias por usar la app!! :D")
        else:
            print("Selecciona una opción válida")
        print("\n\n\n")
        pass
    pass