'''Ejercicio 7: Filtrar números pares
Crea una función llamada `filtrar_pares` que reciba una lista de números enteros y devuelva
una nueva lista solo con los números pares'''

def filtrar_pares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num)
    return resultado

print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # Salida: [2, 4, 6]
print(filtrar_pares([10, 15, 20, 25]))  # Salida: [10, 20]  