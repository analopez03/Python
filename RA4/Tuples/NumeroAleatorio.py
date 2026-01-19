'''Adivina en qué posición está el número n (aleatorio 1-10) en una tupla'''
from random import randint

n = randint(1, 10)
tupla = (1, 2, 4, 5, 8, 2, 9, 7)

print("Número generado:", n)

if n in tupla:
    posicion = tupla.index(n)
    print(f"El número {n} está en la posición {posicion}")
else:
    print(f"El número {n} no está en la tupla")


