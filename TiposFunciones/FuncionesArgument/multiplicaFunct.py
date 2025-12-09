'''tamaño de la pizza por porciones e ingredientes y que salga por pantalla los ingredientes de la pizza y el tamaño
usando argumentos '''

def crear_pizza(tamaño, *ingredientes):
    print(f"\nHaciendo una pizza de tamaño {tamaño} con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
        
crear_pizza(12, "pepperoni", "champiñones", "extra queso")
crear_pizza(16, "jamón", "piña")