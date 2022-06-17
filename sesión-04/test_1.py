
"""Decoradores en Python"""

"""Creación de función decoradora"""
def funcionA(funcionB):
    """Función interna de la función decoradora"""
    def funcionC():
        print("Antes de ejecutar la función a decorar")
        funcionB()
        print("Después de ejecutar la función a decorar")

    return funcionC()


"""Función a decorar"""
@funcionA
def saludar():
    print("Hola Susana")
