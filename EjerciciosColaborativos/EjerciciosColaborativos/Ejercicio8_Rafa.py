'''Pida al usuario una frase. 
Elimine los espacios al inicio y al final (strip()).
 Muestre: La frase en minúsculas (lower()). 
La frase en mayúsculas (upper()). 
La frase con la primera letra en mayúscula (capitalize()). 
Reemplace todas las comas por puntos (replace()). 
Cuente cuántas veces aparece una palabra que el usuario ingresa (count()). 
Verifique si la frase empieza con una vocal (startswith()). 
Muestre cuántas palabras tiene la frase (split()).'''

# Pedir al usuario que ingrese una frase
frase = input("Por favor, ingresa una frase: ")

# Eliminar espacios al inicio y al final
frase = frase.strip()

# Mostrar la frase en minúsculas
print("Frase en minúsculas:", frase.lower())

# Mostrar la frase en mayúsculas
print("Frase en mayúsculas:", frase.upper())

# Mostrar la frase con la primera letra en mayúscula
print("Frase con la primera letra en mayúscula:", frase.capitalize())

# Reemplazar todas las comas por puntos
frase_sin_comas = frase.replace(',', '.')
print("Frase con comas reemplazadas por puntos:", frase_sin_comas)

# Pedir al usuario que ingrese una palabra para contar
palabra_a_contar = input("Ingresa una palabra para contar cuántas veces aparece en la frase: ")

# Contar cuántas veces aparece la palabra en la frase
conteo_palabra = frase.count(palabra_a_contar)
print(f"La palabra '{palabra_a_contar}' aparece {conteo_palabra} veces en la frase.")

# Verificar si la frase empieza con una vocal
vocales = 'aeiouAEIOU'
empieza_con_vocal = frase.startswith(tuple(vocales))
if empieza_con_vocal:
    print("La frase empieza con una vocal.")
else:
    print("La frase no empieza con una vocal.")

# Contar cuántas palabras tiene la frase
palabras = frase.split()
numero_de_palabras = len(palabras)
print("Número de palabras en la frase:", numero_de_palabras)

