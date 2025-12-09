'''Ejercicio 2: Cálculo de precio con IVA
Crea una función llamada `calcular_precio` que reciba:
- precio_base (float)
- iva (float), como argumento por palabra clave, con valor por defecto 21
La función debe devolver el precio final con el IVA aplicado.'''

def calcular_precio(precio_base, iva = 21):
    precio_final = precio_base + (precio_base * iva / 100)
    return precio_final

print(calcular_precio(100))  # Salida: 121.0
print(calcular_precio(250))  # Salida: 302.5