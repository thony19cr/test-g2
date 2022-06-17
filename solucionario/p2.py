"""

    2. Usando el concepto y funciones de lista, realizar un programa con las siguiente características:
    Reglas:
    - Crear una lista con 10 valores random o alatorios
    - Llenar otra lista con sus cubos.
    - Llenar una lista nueva con sus cuadrados.
    - Mostrar de manera inversa la suma de ambas listas.

"""

import random

miLista = []

for i in range(10):
    miLista.append(random.randrange(1, 20))

print("Lista inicial es: {}".format(miLista))

listaCuadrados = []
listaCubos = []

# Agregando los cuadrados de la lista inicial a una nueva lista
for j in miLista:
    listaCuadrados.append(j**2)

print("Lista de cuadrados es: {}".format(listaCuadrados))

# Agregando los cuboss de la lista inicial a una nueva lista
for k in miLista:
    listaCubos.append(k**3)

print("Lista de Cubos es: {}".format(listaCubos))

# Sumando las dos nuevas listas
sumaListas = listaCuadrados + listaCubos

# Invirtiendo la suma de las listas
sumaListas.reverse()

print("Lista inversa de la suma de ambas listas es: {}".format(sumaListas))
