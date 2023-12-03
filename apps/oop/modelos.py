
# Creamos clase Task
# La palabra self indica la instancia en sí de la clase (this en otros lenguajes)
# Al poner self en las funciones indicamos que recibiremos todas las propiedades de la clase
class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def save_task(self):
        pass

tarea = Task("Tarea 1", "Descripción de la tarea 1")