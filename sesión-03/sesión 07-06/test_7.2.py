
"""Gestión de errores"""
"""Estructura y uso"""

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
    except: #Aquí adentro se actvará una acción si ocurre cierto tipo de erro dentro del 'try'
        print("No es un valor entero...")
