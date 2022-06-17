
"""
2. Pedir números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos
(utilizando una función que realice dicha suma).
"""

def sumarDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = int(numero/10)
    return suma


num = int(input("Ingrese número a procesar: "))
while num!=0:
    print("Suma: ", sumarDigitos(num))
    num = int(input("Ingrese número a procesar: "))
