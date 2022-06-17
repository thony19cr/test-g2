
"""Entradas y salidas con Python"""

edad = input("Por favor ingrese su edad: ")
print("El tipo  de mi variable edad es", type(edad))

talla = input("Ingrese su talla en metros: ")


"""Conviritendo nuestra edad"""
print("El nuevo tipo de dato de la variable edad es", type(int(edad)))
print("El nuevo tipo de dato de la variable edad es", type(int(edad)))

"""Conviritendo el valor de nuestra variable"""
print("El nuevo tipo de dato de mi variable talla es: ", type(float(talla)))
print("Al convertir mi nuevo valor a tipo entero: ", type(int(float(talla))))

print("Al convertir mi nuevo valor a tipo entero tiene como dato lo siguiente: ", int(float(talla)))
