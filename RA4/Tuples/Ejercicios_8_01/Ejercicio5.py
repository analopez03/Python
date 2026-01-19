'''Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
● El número de elementos pares.
● El número de elementos impares.
● La suma total.'''

def analizar_numeros(numeros):
    par = 0
    impar = 0

    for i in numeros:
        if i % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

    suma = len(numeros)
    return (par, impar, suma)

numeros = [1, 2, 3, 4, 5]
print(analizar_numeros(numeros))



