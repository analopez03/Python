'''La funcion se llama ganador y me selecciona un ganador aleatorio, yo le paso los nombres y el total de las personas
y me devuelve uno de esos nombres de forma aleatoria'''

import random
def ganador(total_personas, *nombres):
    ganador_elegido = random.choice(nombres)
    return f"El ganador es: {ganador_elegido}"

print(ganador(3, "Ana", "Luis", "Carlos"))