'''Ejercicio 1: Saludo personalizado
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.'''

def saludar(nombre, saludo = "Hola"):
    return f"{saludo} {nombre}"

print(saludar(nombre="Ana"))  # Salida: Hola Ana
print(saludar(nombre="Luis"))  # Salida: Hola Luis