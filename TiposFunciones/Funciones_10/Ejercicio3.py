'''Ejercicio 3: Crear usuario con lista
Crea una función llamada `crear_usuario` que reciba los siguientes argumentos por palabra
clave:
- nombre (str)
- email (str)
- activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos con los datos del usuario en
el orden: [nombre, email, activo].'''

def crear_usuario(nombre, email, activo = True):
    resultado = []
    if activo:
        resultado = [nombre, email, activo]
        return resultado
    else:
        return resultado

print(crear_usuario(nombre="Carlos", email="carlos@gmail.com"))  # Salida: ['Carlos', 'carlos@gmail.com', True]
print(crear_usuario(nombre="Marta", email="marta@gmail.com", activo=False))  # Salida: []