
"""Ejercicios de Listas"""

"""Crear una lista con 10 valroes aleatorios"""
"""Ordenar los elementos de menos a mayor"""

import random

miLista = []

for indice in range(1, 11):
    miLista.append(random.randint(1, 30))

"""Ordenando nuestra lista"""
miLista.sort()

for numero in miLista:
    print(numero, " ", end="")
