'''Modifica la cadena “               este ejercicio es muy complicado            ” 
para que el ejercicio sea facilísimo  y cada una de las palabras comience en mayúsculas y 
sin espacios y luego imprimelo invertido, ademas busca el indice de la palabra complicado.'''

cadena = "               este ejercicio es muy complicado            "
cadena_modificada = cadena.strip().replace("complicado", "facilísimo").title()
cadena_invertida = cadena_modificada[::-1]
indice_complicado = cadena_modificada.find("Facilísimo")

print(cadena_invertida)
print(f'El indice de la palabra "facilísimo" es: {indice_complicado}')