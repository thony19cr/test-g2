
"""POO en Python"""
"""Clases y uso de métodos"""

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

carro1 = Carro("Azul", 15)

print("La velocidad inicial de mi carro 1 es: ", carro1.velocidad)

carro1.acelera()
carro1.acelera()
carro1.acelera()

print("La velocidad final de mi carro luego de acelerarlo tres veces es: ", carro1.velocidad)

carro1.frena()
carro1.frena()

print("Mi nueva velocidad después de aplicar su freno dos veces es: ", carro1.velocidad)
