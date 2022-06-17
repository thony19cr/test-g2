
"""1. Pedir a un usuario ingresar su dirección email. Imprimir un mensaje indicando si la dirección
es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene
el símbolo "@"."""


def validar(email):
    caracterPedido = "@"
    for caracter in email:
        if caracter == caracterPedido:
            return True
    return False


emailUsuario = input("Ingresa tu emaiL: ")

if validar(emailUsuario):
    print("Email válido")
else:
    print("Email inválido")
