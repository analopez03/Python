'''Crea una función convertir_temperatura(celsius) que reciba una
temperatura en grados Celsius y devuelva una tupla con:
● La temperatura en Fahrenheit.
● La temperatura en Kelvin.'''

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)

celsius = 48
print(convertir_temperatura(celsius))
