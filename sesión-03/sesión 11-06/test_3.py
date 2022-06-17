
"""Manejo de archivos"""

"""w: Abre el archivo para poder escribir sobre el"""
file = open("my_files/file.txt", "w")

file.write("Lenguaje multiplataforma: Python\n")
file.write("Está basado en POO\n")
file.write("Basado en diferentes paradigamas de programación")

file = open("my_files/file.txt", "r")

print("Nuestro file tiene el siguiente contenido: ", file.read())

"""Cierre del archivo"""
file.close()
