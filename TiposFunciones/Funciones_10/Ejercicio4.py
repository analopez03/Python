'''Ejercicio 4: Formatear nombre completo
Crea una función llamada `formatear_nombre` que reciba:
- nombre (str)
- apellido (str)
- orden (str), con valor por defecto "nombre_apellido" (el otro valor que podría tomar sería
apellido_nombre)
La función debe devolver el nombre completo en el orden indicado.'''

def formatear_nombre(nombre, apellido, orden = "nombre_apellido"):
    if orden == "nombre_apellido":
        return f"{nombre} {apellido}"
    elif orden == "apellido_nombre":
        return f"{apellido} {nombre}"
    else:
        return "Orden no válido"
    
print(formatear_nombre("Ana", "López"))  # Salida: Ana López
print(formatear_nombre("Ana", "López", orden="apellido_nombre"))  # Salida: López Ana