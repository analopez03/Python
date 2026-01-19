'''Crea una función procesar_cadena(cadena) que devuelva una tupla con:
● La cadena en mayúsculas.
● La cadena en minúsculas.
● La longitud de la cadena.'''

def procesar_cadena(cadena):
    cadenaMayus = cadena.upper()
    cadenaMinus = cadena.lower()
    longitud = len(cadena)
    return (cadenaMayus, cadenaMinus, longitud)

cadena = "Hola buenas tardes"
print(procesar_cadena(cadena))