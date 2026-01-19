'''Escribir un programa que guarde en una variable
el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

divisas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

divisa = input('Ingresa una divisa: ')

if divisa.title() in divisas:
    print(divisas[divisa])
else:
    print('El divisa no es valido')