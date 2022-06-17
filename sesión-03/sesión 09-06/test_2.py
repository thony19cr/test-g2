
"""Manejo de excepciones"""

"""Manejo del error de división entre cero y tipo de datos"""
"""Múltiples excepts en una sóla línea"""

try:
    #val1 = 5/0
    val2 = 2 + "Hola Pythonystas"
except (ZeroDivisionError, TypeError):
    print("Exepción División entre cero/Typerror")