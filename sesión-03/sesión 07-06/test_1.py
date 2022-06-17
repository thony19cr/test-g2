
"""POO en Python"""
"""Clases y atributos de datos"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Contructor: Valores que va a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro1 = Carro("Rojo", 20)

print("El color de mi pirmer carro es: ", carro1.color)

carro2 = Carro("Blanco", 30)
"""Se le asginará un atributo de dato a la instancia de nuestro segundo carro"""

carro2.marchas = 1000

print("El número de marchas de mi carro es: ", carro2.marchas)

"""No esposible llamar un atributo de dato que se le ha asigando a otra instancia de la clase"""
print("El número de marchas de mi primer carro es: ", carro1.marchas)
