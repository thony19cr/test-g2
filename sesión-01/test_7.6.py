
"""Estructura de datos"""

"""Listas: Cantidad de veces que se repite un elemento en una lista"""

lista = ["Python", "Java", "php", "Ruby"]

lista.append("Python")
lista.append("Python")
lista.append("Ruby")

print("Mi nueva lista es: ", lista)
print("La cantidad de veces que se repite 'Python' es: ", lista.count("Python"))
print("La cantidad de veces que se repite 'Ruby' es: ", lista.count("Ruby"))
