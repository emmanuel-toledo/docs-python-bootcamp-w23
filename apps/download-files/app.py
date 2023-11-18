## Ejemplo 1:
## Descargamos un archivo y lo almacenamos localmente.
# from urllib import request
# remote_url = 'https://www.google.com/robots.txt' # Url del archivo remota
# local_file = 'archivo.txt' # Ruta y nombre del archivo a guardar localmente
# request.urlretrieve(remote_url, local_file) # Guardamos archivo localmente



## Instalaciones de paquetes de forma global:
### $ py -m pip install requests ## Instalar paquete requests
### $ py -m pip uninstall requests ## Desinstalar un paquete
### $ py -m pip freeze ## Consultar lista de paquetes instalados
### $ py -m pip freeze > requirements.txt ## Guardar en un archivo las librerías instaladas
### $ py -m pip install -r requirements.txt ## Instalar paquetes a partir de un archivo de librerías
### Las versiones de los paquetes cambian conforme pasa el tiempo, es importante considerar la versión con la que se esta trabajando de cada paquete.

## Podemos generar entornos virtuales de Python, es como una instancia adicional de python de forma local.
### $ py -m venv {nombre de entorno}
### py -m venv venv 

### Podemos ejecutar comandos de python dentro del entorno para instalar librerías y consultar las existentes, serán completamente a parte de las que tenemos cuando no estamos dentro del entorno virutal:
### $ py -m pip install requests
### $ py -m pip freeze

## Para activar un entorno virtual que ya creamos antes ejecutamos:
### Windows: $ .\{nombre entonro}\Scripts\activate ||| .\venv\Scripts\activate
### Linux: $ source venv/bin/activate

## Para desactivar un entorno virtual
### deactivate


## Ejemplo 2:
## Dentro del entorno venv
import requests
remote_url = 'https://www.google.com/robots.txt' # Url del archivo remota
local_file = 'archivo.txt' # Ruta y nombre del archivo a guardar localmente
data = requests.get(remote_url, local_file) # Descargamos el archivo
# Escribimos en nuestro archivo el contenido de la descarga del documento
with open(local_file, 'wb') as file:
    file.write(data.content)


# Se recomienda tener por cada proyecto un ambiente virtual debido a las librerías y versiones de las mismas que se usan.
# No se debe de guardar un entorno virtual en git, ya que aumenta mucho el peso del repositorio.