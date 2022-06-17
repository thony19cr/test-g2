
"""Uso de la librería de fechas y tiempos"""
"""Comparación de fechas"""

import datetime

fecha1 = datetime.datetime(2014, 4, 13) #Tipo de dato datetime
fecha2 = datetime.datetime(2014, 4, 15) #Tipo de dato datetime

if fecha1 == fecha2:
    print("Nacieron el mismo día")
elif fecha1 < fecha2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")