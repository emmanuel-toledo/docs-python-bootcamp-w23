# Comandos de la practica

```
# Si no existe el ambiente hay que crearlo.
py -m venv venv

# Nos movemos al ambiente creado.
.\venv\Scripts\activate

# Instalamos las librerías necesarias.
py -m pip install Django

# Validar versión de django
py -m django --version

# Creamos proyecto llamado core
django-admin startproject core

# Nos movemos a core
cd core

# Vemos una serie de comandos que podemos ejecutar por medio del archivo manage.py
py .\manage.py

# Ejecuta el servidor
py .\manage.py runserver

# Podemos acceder al servidor por medio de los siguientes enlaces:
http://127.0.0.1:8000/ ó http://localhost:8000/

# Cambiar el puerto del servidor
py .\manage.py runserver 7000

# http://localhost:7000/test : Regresa 404 con mensaje Debug
# http://localhost:7000/admin = regresa 200

# Si colocamos en settings.py la variable DEBUG en False, será necesario configurar los ALLOWED_HOSTS = ["*"]
py .\manage.py runserver 7000
# http://localhost:7000/test : Regresa 404 con página predefinida 404 de DJANGO

# Crear aplicación llamada tasks (no veremos mensaje pero si un nuevo folder llamado tasks)
py .\manage.py startapp tasks

# Crear nueva migration con base a modelos creados.
py .\manage.py makemigrations

# Aplicamos una migración
py .\manage.py migrate
```
