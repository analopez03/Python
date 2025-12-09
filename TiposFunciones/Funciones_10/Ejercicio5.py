'''Ejercicio 5: Calcular descuento
Crea una función llamada `calcular_descuento` que reciba:
- precio_original (float)
- descuento (float), como argumento por palabra clave, con valor por defecto 10
La función debe devolver el precio final tras aplicar el descuento.'''

def calcular_descuento(precio_original, descuento = 10):
    precio_final = precio_original - (precio_original * descuento / 100)
    return precio_final

print(calcular_descuento(200))  # Salida: 180.0
print(calcular_descuento(150, descuento = 20))  # Salida: 120.0