'''Creamos un ejercicio que pida dos cadenas, las pase a minusculas, si son iguales que las una y
las bocales las cambie por mayusculas y si no son iguales que las concatene y las muestre en mayusculas'''

cad = input("Introduce la primera cadena: ")
cad2 = input("Introduce la segunda cadena: ")

cad = cad.lower()
cad2 = cad2.lower()
if cad == cad2:
    cad_unida = cad + cad2
    cad_final = ""
    for letra in cad_unida:
        if letra in "aeiou":
            cad_final += letra.upper()
        else:
            cad_final += letra
    print("Las cadenas unidas con vocales en mayusculas son:", cad_final)
else:
    cad_concat = cad + cad2
    print("Las cadenas concatenadas en mayusculas son:", cad_concat.upper())