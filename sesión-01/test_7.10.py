
"""Estructura de dato: Lista"""

"""Elminar un dato de la lista indicando el índice, usando: 'del'"""

lista = []
lista.append(2022)
lista.append("Mayo")
lista.append("Python Módulo I")
lista.append(30)

print(lista)

del lista[1]

print(lista)

"""No es posible eliminar un elemento fuera del rango de índces de la lista"""
#del lista[5]
#print(lista)
