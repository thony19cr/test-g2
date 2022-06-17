
"""Ejercicio 01"""

"""Crea tu primer diccionario con los campos de: tecnología y tipo."""

miDiccionario = {"nombre": "Amazon Web Services", "tipo": "cloud"}

"""Convirtiendo un dicconario a una lista"""

print(list(miDiccionario))
miLista = list(miDiccionario.values())
"""Agregando un nuevo key a nuestro diccionario"""

miDiccionario['antiguedad'] = 16
print(miDiccionario)

"""Verificar valor en diccionario"""
print(miLista)
varComprobacion = "Amazon Web Services" in miLista

print("Valor de comprobación de dato en mi lista", varComprobacion)

"""Creación de un diccionario sin varaible"""
print(dict([("herramienta", "Scrum")]))
