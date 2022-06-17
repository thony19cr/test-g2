
"""Uso de la librería de fechas y tiempos"""
"""Conversión total del tiempo"""

from datetime import datetime

"""Uso del timestamp"""
timeNow = datetime.strptime("2022/02/01 18:40:10", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversión de nuestro valor en timenow es:", timeNow)
