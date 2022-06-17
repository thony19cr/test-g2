
"""Herencia"""
"""Herencia múltiple"""

class A:
    def imprimirA(self):
        print("a")

class B:
    def imprimirB(self):
        print("b")


"""Aplicando la herencia múltiple"""
class C(A, B):
    def imprimirC(self):
        print("c")


varC = C()
varC.imprimirA()
varC.imprimirB()
varC.imprimirC()
