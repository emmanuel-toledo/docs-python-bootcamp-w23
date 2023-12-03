# Podemos ejecutar la función sonido() de más de un objeto con la misma función.
def a_cantar(animal):
    animal.sonido()

class Perro:
    def sonido(self):
        print("Guau!")

class Gato:
    def sonido(self):
        print("Miau!")

class Vaca:
    def sonido(self):
        print("Muuuuuu!")

perro = Perro()
gato = Gato()
vaca = Vaca()

granja = [perro, gato, vaca]

for animal in granja:
    a_cantar(animal)
