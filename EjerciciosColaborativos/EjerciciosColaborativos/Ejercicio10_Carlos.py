'''Recibir dos cadenas de caracteres y contar sus vocales para después sumarlas. 
por otra parte combinar las dos cadenas y remplazar cada carácter que este en una posición impar por una “C”.'''

def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    return sum(1 for char in cadena if char in vocales)

def combinar_y_reemplazar(cadena1, cadena2):
    combinada = cadena1 + cadena2
    resultado = ''
    for i, char in enumerate(combinada):
        if i % 2 != 0:
            resultado += 'C'
        else:
            resultado += char
    return resultado

# Pedir al usuario que ingrese dos cadenas de caracteres
cadena1 = input("Por favor, ingresa la primera cadena de caracteres: ")
cadena2 = input("Por favor, ingresa la segunda cadena de caracteres: ")

# Contar las vocales en ambas cadenas
vocales_cadena1 = contar_vocales(cadena1)
vocales_cadena2 = contar_vocales(cadena2)
total_vocales = vocales_cadena1 + vocales_cadena2
print(f"Número total de vocales en ambas cadenas: {total_vocales}")

# Combinar las dos cadenas y reemplazar caracteres en posiciones impares por "C"
cadena_modificada = combinar_y_reemplazar(cadena1, cadena2)
print("Cadena combinada con caracteres en posiciones impares reemplazados por 'C':", cadena_modificada)


