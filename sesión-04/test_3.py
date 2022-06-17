
"""Decoradores en Python"""
"""Creación de función decoradora"""

def funcionA(funcionB):
    def funcionC(*args, **kwargs):

        print("Antes de ejecutar a la función a decorar")

        resultado = funcionB(*args, **kwargs)

        print("Después de ejecutar a la función a decorar")

        return resultado

    return funcionC

@funcionA
def suma(a, b, c):
    s = a + b + c
    return print(s)


suma(30, 40, 70)
