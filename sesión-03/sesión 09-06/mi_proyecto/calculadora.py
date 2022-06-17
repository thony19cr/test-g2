
#from funciones import suma, resta, multiplicación, division
from funciones import *

x = int(input("Ingrese un valor"))
y = int(input("Ingrese un segundo valor"))

sum = suma(x, y)
print("El resultado de la suma de sus dos valores es:", sum)

div = division(x, y)
print("El resultado de la divisón es:", div)

res = resta(x, y)
print("El resultado de nuestra resta es:", res)
