'''Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.'''

def calcular_estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)
    return minimo, maximo, media

numeros = [4, 8, 15, 16, 23, 42]
print(calcular_estadisticas(numeros))



