'''Vamos a definir una cadena y la vamos a pasar a minusculas, eliminar los espacios
y las letras pares las vamos a cambiar por asteriscos'''

cadena = "Esternocleidomastoideo y burrata"
cadena = cadena.lower().replace(" ", "")
nueva_cadena = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        nueva_cadena += '*'
    else:
        nueva_cadena += cadena[i]

print("Cadena original:", cadena)
print("Nueva cadena:", nueva_cadena)

