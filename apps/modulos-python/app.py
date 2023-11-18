from mathloop.math_func import suma, resta, multiplicacion, division
from mathloop.constants import PI

def main():
    print("Suma: ", suma(20, 10))
    print("Resta: ", resta(20, 10))
    print("Multiplicación: ", multiplicacion(20, 10))
    print("División: ", division(20, 10))
    print("Constante PI: ", PI)

# Validamos si el archivo app.py se esta ejecutando de manera directa, no por importación.
# Otra forma de verlo es si usamos el comando 'py app.py'.
# Las variables globales de python inician con __ y terminan con __, a los módulos que importamos en nuestro
# archivo, python también les coloca un valor diferente a __name__.

# A esta expresión se le conoce como punto de inicio y punto de entrada
if __name__ == "__main__":
    main()


## Notas adicionales:
## Cuando ejecutamos el comando py app.py, genera una carpeta llamada _pycache_ que es un archivo compilado de python para llevar a cabo la ejecución del código.
