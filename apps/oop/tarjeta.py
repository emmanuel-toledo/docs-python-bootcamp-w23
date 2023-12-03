import random

# Todas las funciones que comienzan con __ y terminan con __ son usualmente nativas de Python.
class Tarjeta:

    # Solo puedes tener un constructor en Python
    # Se manda a llamar cuando hacemos algo como lo siguiente:
    # tarjeta = Tarjeta()
    def __init__(self, numero_tarjeta, titular, balance = None, fecha_caducidad = None, pin = None, entidad_emisora = None, is_active = False):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.balance = balance
        self.fecha_caducidad = fecha_caducidad
        self.__pin = random.randint(1000, 9999)
        self.entidad_emisora = entidad_emisora
        self.is_active = is_active

    # Función tipicamente utilizada para mostrar una representación de una instancia de una clase
    # Se manda a llamar de forma automatica cuando hacemos un print(tarjeta). (instancia de tarjeta)
    def __repr__(self):
        return f'Tarjeta: {self.numero_tarjeta} - {self.titular}'
    
    def activar(self):
        self.is_active = True
        print(f'Tarjeta activada: {self.numero_tarjeta}')

    def desactivar(self):
        self.is_active = False
        print(f'Tarjeta desactivada: {self.numero_tarjeta}')
    
    def comprar(self, cantidad):
        self.balance -= cantidad
        print(f'Compra registrada: {self.numero_tarjeta}')
        print(f'Balance actual: {self.balance}')

    # Getter de cada propiedad
    def get_pin(self):
        return self.__pin
    
    # Setter de cada propiedad
    def set_pin(self, pin): # Public
        self.__pin = pin

    # Hacemos que identifiquen una función o propiedad privada, usando un _
    def _logger(self): # Private
        print("Logger registrado")


class TarjetaCredito(Tarjeta):
    def comprar(self, cantidad):
        self.balance -= cantidad
        print(f'Compra registrada: {self.numero_tarjeta}')
        print(f'Balance actual: {self.balance}')
        self.cashback(cantidad)
    
    def cashback(self, cantidad):
        self.balance += cantidad * 0.05
        print(f'Cashback registrado: {self.numero_tarjeta}')
        print(f'Balance actual: {self.balance}')

class TarjetaDebito(Tarjeta):
    def comprar(self, cantidad):
        self.balance -= cantidad
        print(f'Compra registrada: {self.numero_tarjeta}')
        print(f'Balance actual: {self.balance}')

tarjeta = TarjetaCredito(numero_tarjeta = "12345678", titular = "Juan", balance = 1000, 
                  fecha_caducidad = "12/2024", entidad_emisora = "BBVA", is_active = True)

tarjeta.activar()
tarjeta.comprar(1000)
tarjeta.set_pin(3254)
print(tarjeta.get_pin())

tarjeta._logger() # Esto esta mal, ya que es función privada