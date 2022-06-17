
"""Manejo de excepciones"""

"""Manejo del error de división entre cero y tipo de datos"""
"""Múltiples excepts"""

try:
    #val1 = 5/0
    val2 = 2 + "Hola Pythonystas"
except ZeroDivisionError:
    print("No es posible hacer una división entre cero!!")
except TypeError:
    print("Problemas de tipos de datos!!")
