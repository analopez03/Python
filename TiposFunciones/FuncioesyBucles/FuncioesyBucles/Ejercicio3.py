'''import random

def adivina_numero(numero_secreto):
    print("Adivina el número (entre 1 y 100)")

    while True:
        try:
            intento = int(input("Introduce tu intento: "))
            if intento < numero_secreto:
                return print("El número secreto es mayor.")
            elif intento > numero_secreto:
                return print("El número secreto es menor.")
            else:
                return print("¡Felicidades! Has adivinado el número.")
                break
        except ValueError:
            return print("Error: introduce un número válido.")

numero_secreto = random.randint(1, 100)
adivina_numero(numero_secreto)'''

def adivina_numero(numero_secreto, intento):
    try:
        if intento < numero_secreto:
            return "El número secreto es mayor."
        elif intento > numero_secreto:
            return "El número secreto es menor."
        else:
            return "¡Felicidades! Has adivinado el número."
    except ValueError:
        return "Error: introduce un número válido."

import random

numero_secreto = random.randint(1, 100)
print("Adivina el número (entre 1 y 100)")

while True:
    try:
        intento = int(input("Introduce tu intento: "))
        resultado = adivina_numero(numero_secreto, intento)
        print(resultado)
        if resultado == "¡Felicidades! Has adivinado el número.":
            break
    except ValueError:
        print("Error: introduce un número válido.")
