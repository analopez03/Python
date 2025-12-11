'''Pedir por teclado una cadena de texto y “analizarla” con distintas funciones.
Deberá contar la longitud total, contar las letras (mirar str.isaplha()), contar los números, 
contar los caracteres especiales y contar los espacios'''

def analizar_cadena(cadena):
    longitud_total = len(cadena)
    letras = sum(1 for char in cadena if char.isalpha())
    numeros = sum(1 for char in cadena if char.isdigit())
    espacios = sum(1 for char in cadena if char.isspace())
    caracteres_especiales = longitud_total - (letras + numeros + espacios)

    return {
        'longitud_total': longitud_total,
        'letras': letras,
        'numeros': numeros,
        'espacios': espacios,
        'caracteres_especiales': caracteres_especiales
    }
    
# Pedir al usuario que ingrese una cadena de texto
cadena_usuario = input("Por favor, ingresa una cadena de texto: ")
resultado = analizar_cadena(cadena_usuario)
print("Análisis de la cadena ingresada:")
print(f"Longitud total: {resultado['longitud_total']}")
print(f"Número de letras: {resultado['letras']}")
print(f"Número de números: {resultado['numeros']}")
print(f"Número de espacios: {resultado['espacios']}")
print(f"Número de caracteres especiales: {resultado['caracteres_especiales']}")
    