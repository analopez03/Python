'''Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.'''

def analizar_texto(texto):
    num_caracteres = len(texto)

    palabras = texto.split()
    num_palabras = len(palabras)

    if palabras:
        primera_palabra = palabras[0]
    else:
        primera_palabra = ""

    return (num_caracteres, num_palabras, primera_palabra)

texto = "Hola buenas que tal?"
print(analizar_texto(texto))


