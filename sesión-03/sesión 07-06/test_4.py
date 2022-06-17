
"""POO en Python"""
"""Herencia"""

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

"""Aplicando Herencia"""
"""Creando nuestra clase Hija"""
class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro1 = Carro("Rojo", 30)
carroVolador = CarroVolador("Blanco", 40)

print("Colo de mi carro volador es:", carroVolador.color)
print("El estado volando de mi carro voladro es:", carroVolador.estadoVolando)


"""Aquí aplicamos el efecto de herencia al usar el método de la clase padre"""
carroVolador.acelera()

carroVolador.acelera()

print("La velocidad actual de mi carro volador es: ", carroVolador.velocidad)

"""Esto no puede ocurrir"""
#print("El estado en vuelo de mi carro 1 es:", carro1.estadoVolando)
