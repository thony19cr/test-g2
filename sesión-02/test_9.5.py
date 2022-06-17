
"""Manejo de cadenas"""

cadena = "Conexión a base de datos con Python"

cadena2 = cadena.replace(cadena[0:6], "ccc")

print("Cadena con reemplazos tiene el siguiente el valor: {}".format(cadena2))

"""Eliminando espacios en blanco de mi cadena (antes)"""

cadena3 = "     Conexión a base de datos con Python"

cadena4 = cadena3.lstrip()

print("Mi cadena con espacios eliminados: {}".format(cadena4))

"""Eliminando espacios en blanco de mi cadena (después)"""

cadena5 = "Conexión a base de datos con Python       "

cadena6 = cadena5.rstrip()

print("Mi cadena con espacios eliminados: {}".format(cadena6))
