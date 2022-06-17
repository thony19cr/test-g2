
"""Manejo de archivos"""

tecnlogiasBackend = ["Python", "\nJava"]

file = open("my_files/file3.txt", "a+")

file.writelines(tecnlogiasBackend)

file = open("my_files/file3.txt", "r")

for newLine in file:
    if newLine.find("M"):
        print(newLine)
        print("Ha encontrado un varón")

"""Cerrar el archivo aperturado"""
file.close()
