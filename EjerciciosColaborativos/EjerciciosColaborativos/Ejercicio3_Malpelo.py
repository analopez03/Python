'''Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas reglas: 

- Palabras que empiezan por vocal. 
- Palabras que terminan en consonante. 
- Palabras que contienen algún número. 

El programa debe: 

- Separar el texto en palabras. 
- Detectar cuáles cumplen cada condición. 
- Guardarlas en un diccionario con tres listas. 
- Mostrar un informe final indicando las palabras encontradas en cada categoría 
  y cuántas hay en cada una.'''
  
texto = input("Introduce un texto: ")
palabras = texto.split()

resultado = {
    "empiezan_por_vocal": [],
    "terminan_en_consonante": [],
    "contienen_numero": []
}

vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
numeros = "0123456789"

for palabra in palabras:
    if palabra[0] in vocales:
        resultado["empiezan_por_vocal"].append(palabra)
    if palabra[-1] in consonantes:
        resultado["terminan_en_consonante"].append(palabra)
    if any(char in numeros for char in palabra):
        resultado["contienen_numero"].append(palabra)

print("Informe final:")

for categoria, lista in resultado.items():
    print(f"{categoria.replace('_', ' ').capitalize()}: {lista} (Total: {len(lista)})")
    
