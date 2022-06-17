
"""Manejo de archivos"""

tecnologiasBackend = ["\nPython, ", "Java, ", "Ruby, ", "NodeJS"]
tecnologiasFrontend = ["\nAngular, ", "Javascript, ", "ReactJS, ", "Boostrap"]

"""Opertura de nuestro archivo"""

"""a+: Permite escribir varias líneas de código al abrir nuestro archivo"""
"""a+: Escribe nuevas líneas de texto sin borrar las líneas que ya estaban escritas previamente en el archivo"""
file = open("my_files/file2.txt", "a+")

"""writeLines: Permite escriber los datos de una lista"""
file.writelines(tecnologiasBackend)

file.writelines(tecnologiasFrontend)

file = open("my_files/file2.txt", "r")

print("El contenido de nuestro file es:", file.read())

"""Cierre del archivo"""
file.close()

