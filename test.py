'''Pregunta 3'''

nombre = input('Tu nombre: \n')
apellidos = input('Tu apellido: \n')
edad = input('Tu edad: \n')
dni = input('Tu dni: \n')

miDiccionario = {'nombre': nombre, 'apellidos': apellidos, 'edad': edad, 'dni': dni}
print(miDiccionario)
listar = list(miDiccionario.values())
print(listar)

profesion = input('Tu profesion: \n')

miDiccionario['profesion'] = profesion
print(miDiccionario)

del miDiccionario['dni']
print(miDiccionario)
