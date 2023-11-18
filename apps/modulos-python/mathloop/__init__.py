# La carpeta mathloop es un package.
# Un package es un archivo que contiene multiples módulos dentro de si.
# constants.py es un módulo.
# math_func.py es un módulo.

# Siempre que vamos a crear un package debemos de crear un archivo llamado __init__.py

# En este archivo se suele colocar código de configuración o preparación del package.

if __name__ == "__main__":
    print("Llamando al archivo __init__.py de forma directa")
else:
    print("Ejecutando archivo __init__.py de package MathLoop")
    print("Conectando con el package MathLoop")
    print("Nombre del módulo: ", __name__)
    