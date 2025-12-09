'''Modifica la cadena “               este ejercicio es muy complicado            ” 
para que el ejercicio sea facilísimo  y cada una de las palabras comience en mayúsculas y 
sin espacios y luego imprimelo invertido, ademas busca el indice de la palabra complicado.'''
cadena = "               este ejercicio es muy complicado            "
# Eliminar espacios en blanco al inicio y al final
cadena = cadena.strip()
# Reemplazar "complicado" por "facilísimo"
cadena = cadena.replace("complicado", "facilísimo")
# Convertir la primera letra de cada palabra a mayúscula
cadena = cadena.title()
# Invertir la cadena
cadena_invertida = cadena[::-1]
# Buscar el índice de la palabra "complicado"
indice_complicado = cadena.find("Complicado")

# Imprimir los resultados
print("Cadena modificada e invertida:", cadena_invertida)
print("Índice de la palabra 'complicado':", indice_complicado)



    
