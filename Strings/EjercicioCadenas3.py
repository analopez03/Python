'''Vamos a definir una cadena y la vamos a pasar a minusculas, eliminar los espacios
y las letras pares las vamos a cambiar por asteriscos'''

cadena = "Esternocleidomastoideo y burrata"

# Convertimos a minusculas y eliminamos espacios
cadena = cadena.lower().replace(" ", "")

# Reemplazamos las letras en posiciones pares por asteriscos
nueva_cadena = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        nueva_cadena += cadena[i]
    else:
        nueva_cadena += '*'

# Imprimimos los resultados
print("Cadena original:", cadena)
print("Nueva cadena:", nueva_cadena)

