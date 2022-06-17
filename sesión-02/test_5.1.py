
"""Uso del flujo condicional if"""

edad = int(input("Cuál es su edad?: "))

if 0 < edad < 18:
    print("Es usted menor de edad")
elif 18 < edad and edad <65:
    print("Es usted una persona adulta")
elif edad > 65:
    print("Usted es una persona de la tercera edad")
else:
    print("Usted ha ingresado una edad eronea")
