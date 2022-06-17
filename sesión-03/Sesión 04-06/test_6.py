
"""
4.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana
que lo decida.

"""

def primo(numero):
    for i in range(2, numero):
        if numero%i==0:
            return False
    return True

num = int(input("Ingrese número a evaluar: "))
if primo(num):
    print("El número es primo")
else:
    print("El número no es primo")
