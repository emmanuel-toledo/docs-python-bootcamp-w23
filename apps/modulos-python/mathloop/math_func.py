# Si no se define un valor del return, siempre regresará un None

# # Importamos elementos especificos de un archivo
# from constants import PI
# # Importamos todo el módulo (archivo)
# import constants
# # Importamos todo el módulo (archivo) con un alias
# import constants as cst

# Al buscar un archivo que pertenece al mismo package, colocamos un . antes del nombre del módulo para indicar a Python que busque dentro de este mismo package (folder mathloop)
from .constants import PI # Archivo constants.py



def suma(valor1 = None, valor2 = None):
    if valor1 == None or valor2 == None:
        return "No tienes valores válidos"
    resultado = valor1 + valor2
    return resultado

def resta(valor1 = None, valor2 = None):
    if valor1 == None or valor2 == None:
        return "No tienes valores válidos"
    resultado = valor1 - valor2
    return resultado

def multiplicacion(valor1 = None, valor2 = None):
    if valor1 == None or valor2 == None:
        return "No tienes valores válidos"
    resultado = valor1 * valor2
    return resultado

def division(valor1 = None, valor2 = None):
    if valor1 == None or valor2 == None:
        return "No tienes valores válidos"
    resultado = valor1 / valor2
    return resultado

def area_circulo(radio):
    area = PI * (radio ** 2)
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
