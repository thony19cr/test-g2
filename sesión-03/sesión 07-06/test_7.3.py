
"""Gestión de errores"""
"""Gestor de multi errores"""

try:
    """Aquí irá nuestro código A ejecutar inicialmente con posibls errores"""
except IOError:
    """Ejecuta esta sentencia si ocurre un error de localización de archivos"""
except ZeroDivisionError:
    """Ejecuta esta sentencia si ocurre un error de división entre cero"""
except:
    """Ejecutamos esta sentencia a nivel general sino está mapeado en los primeros 'except'"""
