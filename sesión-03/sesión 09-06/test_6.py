
"""Uso de la librería de fechas y tiempos"""

from datetime import date, datetime

import time
"""Uso del date"""

"""Obtener la fecha actual"""
fecha = date.today()
print("La fecha a manejar es la siguiente: ", fecha)

"""Uso del datetime para extraer el año, el mes y el día"""
tiempo = datetime.now()

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Tiempo actual es: ", tiempo)
print("Año actual", anio)
print("Mes actual", mes)
print("Día actual", dia)


"""Uso del datetime para extraer el año, el mes y el día"""
hora = tiempo.hour
minuto = tiempo.minute
segundo =tiempo.second

print("La hora exacta son las: {} con {} minutos y {} segundos".format(hora, minuto, segundo))