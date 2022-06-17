
"""Uso de la librería de fechas y tiempos"""

from datetime import datetime

strFecha = "2/6/2020"

"""
    d: día
    m: mes
    Y: año
"""

conversion = datetime.strptime(strFecha, "%m/%d/%Y")

print("La fecha formateada es: ", conversion)

"""Traer el mes de la fecha con letras: strftime de datetime"""

conversionMes = datetime.strftime(conversion, "%b %d, %Y")
print("Nuestra fecha con cambio en el mes es el siguiente: ", conversionMes)

"""b: reemplaza a 'm' para mostrar el mes literalmente"""
