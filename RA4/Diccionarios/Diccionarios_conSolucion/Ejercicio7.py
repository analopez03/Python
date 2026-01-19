'''Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
el coste total, con el siguiente formato'''

compra = {}

continuar = True

while continuar:
    item = input("Ingresa una articulo: ")
    precio = float(input("Ingresa una precio" + item + ": "))

    compra[item] = precio

    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"

for item, precio in compra.items():
    print(item, " Precio: ", precio)

