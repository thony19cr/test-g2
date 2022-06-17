import json

"""Uso de librería JSON"""
"""Conversión inversa de tipo de dato Python a JSON"""

pythonDict = {"name": "Mary", "edad": 27, "dni": "97349723"}

"""Conversión de tipo de dato JSON: """

dictToJson = json.dumps(pythonDict)
print("El dato convertido a JSON es el siguiente: ", dictToJson)
print("El tipo de dato convertido es de tipo: ", type(dictToJson))
