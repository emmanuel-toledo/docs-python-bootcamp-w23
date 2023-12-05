# Comandos previos a la ejecución de la app

```
# Si no existe el ambiente hay que crearlo.
py -m venv venv

# Nos movemos al ambiente creado.
.\venv\Scripts\activate

# Instalamos las librerías necesarias.
py -m pip install -r requirements.txt

# Para cerrar ambiente.
deactivate
```

# Aplicación de Tareas

Crear una aplicación de Python para terminal y línea de comandos que sea útil para gestionar las tareas a realizar.

Esta aplicación debe contar con un modelo de base de datos que lleve el registro de:
- Nombre de la tarea
- Descripción de la tarea
- Estado de la tarea (Completado, No completado)
- Fecha en la que se creó la tarea.
- Fecha en la que se completó la tarea.

Expectativas de la actividad:
- La aplicación debe correr en la terminal y línea de comandos.
- La aplicación debe utilizar como motor de base de datos sqlite3.
- La aplicación debe contar con un menú interactivo.
- La aplicación debe permitir todas las operaciones básicas de base de datos (CRUD -> CREATE, READ, UPDATE, DELETE).
- La aplicación debe de formatear las respuestas en una estructura de datos tipo JSON (Puede ser una lista de objetos, un diccionario, etc)
- Las fechas en los formatos de respuesta deben mostrarse como: DD/MM/YYYY HH:mm:SS (10/06/2023 08:30:00)
- Dividr la aplicación en pequeños módulos y funciones. Cada archivo no debe exceder las 200 líneas de código.

### Fecha de entrega: 2 de Diciembre de 2023
