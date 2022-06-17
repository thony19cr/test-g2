"""

    3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un programa con los siguientes requerimientos
    Reglas:
    - Crear una diccionario con los keys de nombre, apellidos, edad y dni.
    - Pedir por consola los valores para estos keys.
    - Convertir el diccionario a una lista y mostrar en pantalla el tipo de dato.
    - Agregar un key adicional con el nombre de “profesion”
    - Eliminar el key dni y mostrar el nuevo diccionario.

"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dni = input("Ingrese su DNI: ")

diccionarioPersona = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'dni': dni}

# Convirtiendo a lista mi diccionario
diccionarioALista = list(diccionarioPersona)

print("El tipo de mi nuevo dato es: {}".format(type(diccionarioALista)))

# Agregando un nuevo key a mi diccionario

diccionarioPersona['profesion'] = input("Ingrese su profesión: ")

# Eliminando el key dni

del diccionarioPersona['dni']

# Mostrando mi diccionario actualizado

print("Mi diccionario actualizado es: {}".format(diccionarioPersona))
