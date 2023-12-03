class Cubo:
    # Atributo de clase
    caras = 6
    
    # Constructor
    def __init__(self, nombre, color):
        # Atributos de instancia
        self.nombre = nombre
        self.color = color

    # Métodos de clase
    def soltar(self):
        print(f'Soltando el cubo: {self.nombre}')
    

cubo_de_arena = Cubo(nombre = "sand", color = "white")
cubo_de_madera = Cubo(nombre = "wood", color = "brown")

cubo_de_arena.soltar()
cubo_de_madera.soltar()