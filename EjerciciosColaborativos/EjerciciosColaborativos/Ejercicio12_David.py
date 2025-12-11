'''Enunciado:
Crear una funcion que cuente el numero de letras que tiene un string, el numero de numeros y el numero de espacios.
La funcion debe devolver un string con el siguiente formato:
"tienes X letras, Y numeros y Z espacios"'''

def contar_elementos(cadena):
    letras = sum(1 for char in cadena if char.isalpha())
    numeros = sum(1 for char in cadena if char.isdigit())
    espacios = sum(1 for char in cadena if char.isspace())
    
    return f"tienes {letras} letras, {numeros} numeros y {espacios} espacios"

# Pedir al usuario que ingrese una cadena de texto
cadena_usuario = input("Por favor, ingresa una cadena de texto: ")
resultado = contar_elementos(cadena_usuario)
print(resultado)

