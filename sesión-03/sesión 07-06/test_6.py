
"""POO en Python"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("Guauu")

class Gato():
    def sonido(self):
        print("Miauuu")

class Vaca():
    def sonido(self):
        print("Muuu")

vaca = Vaca()
perro = Perro()
gato = Gato()

listaAnimales = [vaca, perro, gato]

def cantar(animales):
    for animal in animales:
        animal.sonido()

"""Aplicando Polimorfismo: Es el uso de los métodos que tienen como mismo nombre en diferentes clases"""

cantar(listaAnimales)
