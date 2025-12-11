'''Crea una función que reciba un argumento string y 
compruebe si todos los caracteres son mayúsculas'''

def es_mayusculas(texto):
    if texto.isupper():
        return True
    else:
        return False

# Prueba de la función
texto_usuario = input("Introduce un texto: ")
if es_mayusculas(texto_usuario):
    print("Todos los caracteres son mayúsculas.")
else:
    print("No todos los caracteres son mayúsculas.")

