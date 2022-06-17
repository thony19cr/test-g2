
"""POO en Python"""
"""Herencia Múltiple"""

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


class CarroSedan:

    def __init__(self):
        super().__init__()
        self.tamanio = 150

"""Aplicando Herencia Múltiple"""
class CarroVolador(Carro, CarroSedan):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carroVolador = CarroVolador("Negro", 40)

"""Herencia del primer padre"""
print("La velocidad inicial de mi carro volador es: ", carroVolador.velocidad)

"""Herencia del segundo padre"""
print("El tamaño de mi carro volador es: ", carroVolador.tamanio)
