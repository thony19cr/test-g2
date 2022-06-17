
"""Decoradores en Python"""

"""Creación de función decoradora"""
def funcionA(funcionB):
    """Función interna de la función decoradora"""
    def funcionC(*args, **kwargs):    # *args, **kwargs: Recibir N parámetros que tenga la función
        print("Antes de ejecutar la función a decorar") #1er código de código
        resultado = funcionB(*args, **kwargs)
        print("Después de ejecutar la función a decorar") #2do bloque de código

        return resultado
    return funcionC


"""Función a decorar"""
@funcionA
def saludar(nombre):
    return print("Hola {}".format(nombre))


saludo = input("Ingrese su nombre: ")
print(saludar(saludo))
