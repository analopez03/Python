'''Vamos a crear una cadena encriptada, pedimos al usuario que introduzca una cadena
y la pase toda a minusculas y elimine espacios en blanco, las vocales las va a sustituir por números
a = 1, e = 5, i = 9, o = 15, u = 21 y al final nos muestra la cadena encriptada.'''

def encriptar_cadena(cadena):
    cadena = cadena.lower().replace(" ", "")
    sustituciones = {'a': '1', 'e': '5', 'i': '9', 'o': '15', 'u': '21'}
    
    for vocal, numero in sustituciones.items():
        cadena = cadena.replace(vocal, numero)
    
    return cadena

cadena = input("Introduce una cadena para encriptar: ")
cadena_encriptada = encriptar_cadena(cadena)
print("Cadena encriptada:", cadena_encriptada)
