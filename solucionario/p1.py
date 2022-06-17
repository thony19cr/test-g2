"""

    1. Usando los tipos de datos y
    sus conversiones realizar lo siguiente.
    Reglas:
    - Pedir por consola nombre y edad.
    - Edad tiene que ser tipo entero, para esto
    apoyarse de la conversión de datos
    - Identificar los tipos ingresados.
    - Pedir los nombre para dos personales y finalmente
    mostrar en pantalla la suma de ambos.

"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("El tipo de dato del nombre es: ", type(nombre))
print("El tipo de dato de la edad es: ", type(edad))

nombre1 = input("Personal 1 ingrese su nombre: ")
edad1 = int(input("Personal 2 Ingrese su edad: "))

nombre2 = input("Personal 1 Ingrese su nombre: ")
edad2 = int(input("Personal 2 Ingrese su edad: "))

suma = edad1+edad2
print("La suma de las edades de los dos personales es: {}".format(suma))

print("Edad 1", edad1)
