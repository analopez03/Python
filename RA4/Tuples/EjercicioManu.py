'''Tienes dos funciones saludo y despedida creas la lista dos elemenentos saludar y
despedir escribe por teclado a una de las dos, si conincide al elemento de la tupla muestra el resultado
sino un mensaje'''

def saludo():
    return "Hola"

def despedida():
    return "Adios"

comandos = ("saludo", "despedida")

funciones = (saludo, despedida)

buscar = input("Introduce una palabra: ").lower()

if buscar in comandos:
    i = comandos.index(buscar)
    print(funciones[i]())
else:
    print("Elemento no encontrado")




