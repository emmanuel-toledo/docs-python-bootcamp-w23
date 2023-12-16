# Python

Python es un lenguaje de programación con el cual podemos trabajar desde diferentes puntos, frontend, backend e incluso hasta IA.

# Enlaces de apoyo

| Descripción | URL | Observaciones |
| ------------- | ------------- | --- |
| Descargar Python | https://www.python.org/downloads/windows/ | |
| Pypi org | https://pypi.org/ | Similar a nuget.org, buscamos librerías para una necesidad |
| Google colab | https://colab.research.google.com/ | |
| Django | https://www.djangoproject.com/ | ORM de Python |

# Python

Unos aspectos de ```python``` que son importantes son:
- Este lenguaje opta por la simplicidad.
- Es multiparadigma.
- No esta encerrado a un solo tipo de desarrollo.
- Nacio en 1989 por Guido Van Rossum.
- Es el lenguaje oficial de Google, la infraestructura de Instagram lo usa.
- Aprenderlo es sencillo, pero debemos tener cuidado en como lo usamos.

Razones para aprenderlo:
1. Sintaxis simple.
2. Muchas librerías disponibles.
3. Una comunidad de apoyo.
4. Alta demanda laboral.
5. Multipropósito dependiendo el proyecto.
6. Tipado dinámico, no hace falta declararlo.

Los escenarios para usar ```python``` son:
1. Data science
2. Robótica
3. Big Data
4. Machine learning
5. Desarrollo web
6. Seguridad informática

## OOP (ORIENTED OBJECT PROGRAMMING)

OOP: Programación orientada a objetos (POO).

Python hace uso de la programación orientada a objetos en casi todo el tiempo.

Objeto: Elemento de la vida real que puede llegar a tener alguna representación lógica.

Clase: Plantilla de código con representación de un elemento de la vida real que contiene porpiedades o atributos y métodos o funciones. Podemos verlo como un molde de pan.

Propiedades / Atributos: Caracteristicas que conforman a un objeto, por ejemplo un carro, una caracteristica es el color, módelo, etc. Información de un objeto.

Metodos / Funciones: Acciones que puede llevar a cabo un objeto, por ejemplo un carro, puede encender o apagar.

Instancia: Resultado de crear un objeto a partir de una clase. Se creó una instancia (objeto) de una clase.

Abstracción: Resultado de ver objetos de la vida real y definir atributos lógicos de ellos.

## ORM (Object Relational Mapping)

Un ORM nos permite conectar a una base de datos a partir de un módelo de clases, esto permite ahorarnos comandos SQL y preservar la integridad de los datos al no permitir la inyección de código SQL.

Es el concepto con el cual se creó Entity Framework Core.

En Python DJango tiene integrado el uso de un ORM.

Un ORM trabaja con clases y objetos, si conocemos los principios de POO, será facil comprender su uso.

# Deserialization and Serialization

En las API podemos serializar o deserealizar un request o respuesta para cada servicio.

# REST API

Trabaja bajo el esquema Cliente - Servidor.

Permite generar peticiones web con 4 bases principales.
1. URL de acceso a un servicio
2. Método con el que se dispara el servicio
3. Body que es el contenido de una petición
4. Headers que son las cabeceras de como se debe de ejecutar nuestro servicio

# DJANGO

```Django``` es un ORM que nos permite conectar a diferentes (bases de datos)[https://docs.djangoproject.com/en/5.0/topics/install/#database-installation], tales como:
- MariaDB
- MySQL
- PostgreSql
- Oracle
- SQLite

Podemos (instalar django)[https://docs.djangoproject.com/en/5.0/topics/install/#] con el comando:

```
py -m pip install Django

ó

python -m pip install Django
```

Una vez instalado se nos habilita una serie de comandos adicionales, para ver cuales son ejecutamos ```django-admin```.

Podemos inicializar un nuevo proyecto.

```
django-admin startproject {nombre proyecto}

# Creamos proyecto llamado core
django-admin startproject core
```

Se crea una carpeta llamada ```core```, usualmente se trabaja sobre el archivo ```settings.py``` para aplicar configuraciones al proyecto, pero también usaremos el archivo ```urls.py``` que es donde comunmente agregaremos nuestros endpoints de la api.

```manage.py``` es el archivo que administra nuestra aplicación, aquí podemos cargar configuraciones y agregar comandos que serán ejecutados por medio de la línea de comandos.

Si ejecutamos el comando ```manage.py```, veremos una lista de comandos que podemos ejecutar para interactuar con DJANGO.

```
# Ejecuta el servidor
py .\manage.py runserver

# Podemos acceder al servidor por medio de los siguientes enlaces (para cerrar CTL + C):
http://127.0.0.1:8000/
ó
http://localhost:8000/

# Cambiar el puerto del servidor
py .\manage.py runserver 7000
```

```Django``` nos permitió crear nuestro entorno de trabajo con este ORM, pero ahora vamos a crear una aplicación basada en ```Django```.

Todas las aplicaciones de ```Django``` trabajan bajo la arquitectura ```MVC``` (Modelo, Vista, Controlador).

```
# Crear aplicación llamada tasks (no veremos mensaje pero si un nuevo folder llamado tasks)
py .\manage.py startapp tasks
```

Se crearon diferentes archivos y directorios:
- migrations: Directorio donde tendremos registro de todas las migraciones de nuestras clases hacia la base de datos.
- __init__.py: Indica que el directorio tasks es un package.
- admin.py: Registrar los módelos para poder manipularlos directamente en el archivo.
- apps.py: Podemos configurar como se llamará la aplicación así como algunas otras caracteristicas.
- tests.py: Archivo para manejar pruebas unitarias.
- views.py: Vista que se le presentará al usuario.
- models.py: Definimos los módelos de datos que la aplición usará (clases).
- urls.py: Este archivo no existe y es recomendable crearlo, ya que aquí se definen las urls o endpoints de la aplicación, ```Django``` marca usar el archivo ```urls.py``` del directorio core, pero entre más apps se tengan, sería buena práctica dividir que cada aplicación tenga su propio archivo ```urls.py```.

Para este punto ```Django``` no conoce nada sobre la aplicación que creamos, porque no se ah instalado, para hacer eso es demasiado sencillo, simplemente colocamos el nombre que definimos a la aplicación (o bien, es el nombre definido en el archivo ```apps.py```, en este caso tasks), dentro de la variable ```INSTALLED_APPS``` del archivo ```core -> settings.py```.

## Migraciones

Si abrimos el archivo ```db.sqlite3``` veremos que no tenemos nada de esquema cargado.

Cuando ejecutamos ```Django``` vemos el siguiente mensaje. 

```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

Esto nos dice que no tenemos ningun esquema cargado a la base de datos, pero para este tipo de acciones nos ayuda ```Django```.

```
# Aplicamos una migración
py .\manage.py migrate
```

Si consultamos nuevamente el archivo ```db.sqlite3``` veremos las tablas creadas, y si ejecutamos el servidor nuevamente, ya no veremos el mensaje anterior.

Dentro del archivo ```tasks -> models.py``` vamos a generar una clase para crear una tabla en nuestra base de datos.

```
from django.db import models

# Necesario heredar de Model para llevar a cabo la migración.
class Task(models.Model):
    # Definimos el tipo de dato de la columna que tendrá en la base de datos.
    title = models.CharField(max_length=200)

    # Representación del módelo en string.
    def __str__(self) -> str:
        return f"ID: {self.pk} - {self.title}"
```

Antes de migrar a la base de datos el módelo, debemos de crear una migración, para ello hacemos lo siguiente.

```
# Creamos una migración, detectará nuestras clases creadas. 
# Por defecto todas las migraciones a clases sin primary key las creará de forma automatica
# Puede ver el archivo 0001_initial.py 
py .\manage.py makemigrations

# Pendiente una migración
py .\manage.py runserver 7000

# Aplicamos una migración
py .\manage.py migrate
```

## Shell

Para acceder a la ```shell``` de ```django``` hacemos lo siguiente.

```
# Acceder a shell.
py .\manage.py shell

# Podremos ejecutar líneas de código de python.
# Al trabajar con Django, este nos permite trabajar de una manera diferente con los módelos de datos y las clases.

# Importamos modelo Task (DbSet en Entity Framework Core)
>>> from tasks.models import Task

# Obtenemos lista de objetos de la tabla Task
>>> Task.objects.all()

# Creamos un nuevo registro
>>> Task.objects.create(title = "Mi primera tarea creada desde ORM")

# Veremos QuerySet en representación string
>>> Task.objects.all()

# Actualizamos un registro
# Obtener registro con pk o id: 1
>>> tarea_uno = Task.objects.get(pk=1)

# Modificamos el objeto pero no la DB
>>> tarea_uno.title = "Tarea modificada"

# Se guarda el registro en la base de datos
>>> tarea_uno.save()

# Eliminamos un registro
>>> tarea_uno.delete()

# Salir de shell
>>> exit()
```

Si queremos ajustar nuestra estructura de datos en la base de datos podemos hacer lo siguiente.

La clase ```Task``` dentro de ```tasks -> models.py```:

```
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.CharField(default = False)

    # Representación del módelo en string.
    def __str__(self) -> str:
        return f"ID: {self.pk} - {self.title}"
```

Creamos y aplicamos los cambios de la migración.

```
# Creamos migración
py .\manage.py makemigrations

# Aplicamos una migración
py .\manage.py migrate
```

Veremos como la estructura de la base de datos cambio a lo que definimos, podemos hacer lo mismo si borramos una columna, simplemente creamos la migración y la aplicamos.
