word = input('Introduzca una palabra: ')
if word == 'banana':
    print('All right, bananas.')
    
if word < 'banana':
    print('Tu palabra, ' + word + ', va antes banana.')
elif word > 'banana':
    print('Tu palabra, ' + word + ', va despues banana.')
else:
    print('All right, bananas.')
