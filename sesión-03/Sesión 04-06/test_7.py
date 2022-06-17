
"""

5.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito
en el número (en último lugar del número), utilizando para ello una función que calcule la frecuencia.

"""

def frecuencia(numero, digito):

    cantidad = 0
    while numero!=0:
        ultDigito = numero%10
        if ultDigito==digito:
            cantidad = cantidad + 1
        numero = int(numero/10)
    return cantidad

num = int(input("Ingrese un número: "))
uDigito = int(input("Ingrese dígito a encontrar: "))
print("Frecuencia del dígito {uDigito} en el número {num} es de: {frecuencia}".format(num=num, uDigito=uDigito,
                                                                            frecuencia=frecuencia(num, uDigito)))
