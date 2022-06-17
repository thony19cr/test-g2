
import json

class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre


nombreEmpleado = Empleado("Luis")

empleado = {"nombre": nombreEmpleado}
empleadoToJson = json.dumps(empleado)

print("El dato de nuestra nueva variable es: ", empleadoToJson)
