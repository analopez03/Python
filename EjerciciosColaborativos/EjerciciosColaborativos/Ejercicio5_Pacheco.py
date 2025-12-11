'''A través de una función, introduciendo una cadena por parámetro, 
devolver la longitud, devolver la cadena en minúsculas y 
devolver las ultimas 5 letras de la cadena. '''

def analizar_cadena(cadena):
    longitud = len(cadena)
    minusculas = cadena.lower()
    ultimas_cinco = cadena[-5:]

    return longitud, minusculas, ultimas_cinco

# Prueba de la función
texto_usuario = input("Introduce una cadena de texto: ")
longitud, minusculas, ultimas_cinco = analizar_cadena(texto_usuario)
print(f'Longitud de la cadena: {longitud}')
print(f'Cadena en minúsculas: {minusculas}')
print(f'Últimas 5 letras de la cadena: {ultimas_cinco}')

