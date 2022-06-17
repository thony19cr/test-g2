
"""Uso de módulo en Python"""
"""Uso debido del from para no traer a sus demás método y no provocar una sobre carga de memoria"""

from math import sqrt as raiz

x = int(input("Ingrese un número base"))

"""sqrt: nos sirve para la sacar la raíz cuadrada de un número"""

valorRaiz = raiz(x)

print("La raíz cuadrada de su número ingresado es: ", valorRaiz)
