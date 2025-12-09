'''Ejercicio 8: Generar tabla de multiplicar
Crea una función llamada `tabla_multiplicar` que reciba:
- numero (int)
- hasta (int), como argumento por palabra clave, con valor por defecto 10
La función debe devolver una lista con la tabla de multiplicar del número hasta el valor
indicado.'''

def tabla_multiplicar(numero, hasta = 10):
    resultado = []
    for i in range(1, hasta + 1):
        resultado.append(numero * i)
    return resultado

print(tabla_multiplicar(5))  # Salida: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(tabla_multiplicar(3))  # Salida: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]   