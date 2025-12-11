'''Volviendo a Messenger

Pide al usuario una oración completa y el programa debe averiguar cuántas palabras tiene esa oración.
Si ese número es par, convierte las letras pares a mayúsculas y las impares a minúsculas y devuelve esa frase convertida.
Si el número es impar, devuelve la frase con las palabras con el orden invertido.
Modulen pls
frase = "Estoy estudiando Python y no quiero suspender'''

def analizar_frase(frase):
    palabras = frase.split()
    numero_de_palabras = len(palabras)

    if numero_de_palabras % 2 == 0:
        frase_convertida = ''
        for i, char in enumerate(frase):
            if char.isalpha():
                if i % 2 == 0:
                    frase_convertida += char.upper()
                else:
                    frase_convertida += char.lower()
            else:
                frase_convertida += char
        return frase_convertida
    else:
        palabras_invertidas = palabras[::-1]
        return ' '.join(palabras_invertidas)
    
# Pedir al usuario que ingrese una oración completa
oracion_usuario = input("Por favor, ingresa una oración completa: ")
resultado = analizar_frase(oracion_usuario)
print("Resultado:", resultado)  

