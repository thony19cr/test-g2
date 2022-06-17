
"""POO en Python"""
"""Encapsulamiento"""

class A():

    def __init__(self):
        """Encapsulamiento"""
        self.inicial = False
        self._contador = 0  #Definiendo mis atributos como privados

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B():
    def __init__(self):
        """Encapsulamiento"""
        self.inicial = True
        self.__contador = 0  #Definiendo mis atributos como privados

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador


varA = A()
varA._contador
varA.inicial = True
varA.incrementa()
varA.incrementa()
print(varA.cuenta())
print(varA.inicial)
"""Si es posible inivacrlo pero sólo se hace referencia que ese valor está encapsulado"""
print("Contador A: ", varA._contador)


varB = B()
varB.inicial = False
varB.incrementa()
varB.incrementa()
varB.incrementa()

print(varB.cuenta())
print(varB.inicial)
"""No es posible invocarlo por que el encapsulamiento es fuerte por los dos guiones abajo."""
print("Contador B: ", varB.__contador)
