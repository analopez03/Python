'''def analisis_notas(notas):
    suma = 0
    cont = 0
    nota_alta = notas[0]
    nota_baja = notas[0]


    for nota in notas:
        if nota >= 5:
            cont += 1
        
        suma += nota
        
        media = round((suma / len(notas)), 2)
        
        if nota_baja > nota:
            nota_baja = nota

        if nota_alta < nota:
            nota_alta = nota

    print(f'El total de alumnos aprobados es: {cont}')
    print(f'La nota media del grupo es: {media}')
    print(f'La nota más alta es: {nota_alta} y la más baja es: {nota_baja}')

notas = [2, 1, 10, 6, 7, 9, 3]
analisis_notas()'''

def analisis_notas(notas):
    if not notas:  
        return None, None, None, 0
    notasCinco = []
    suma = 0
    cont_aprobados = 0
    nota_alta = notas[0]
    nota_baja = notas[0]

    for nota in notas:
        suma += nota

        if nota >= 5:
            cont_aprobados += 1

        if nota > nota_alta:
            nota_alta = nota

        if nota < nota_baja:
            nota_baja = nota

    media = round(suma / len(notas), 2)
    
    for nota in notas:
        if nota >= 5:
            notasCinco.append(nota)

    # Devuelve todos los valores calculados por orden
    return media, nota_alta, nota_baja, cont_aprobados, notasCinco

notas = [2, 1, 10, 6, 7, 9, 3, 5, 8, 4]

# Asigna los valores por orden que hay dentro de la función
media, alta, baja, aprobados, notasCinco = analisis_notas(notas) 

print(f"Media: {media}")
print(f"Nota más alta: {alta}")
print(f"Nota más baja: {baja}")
print(f"Total de aprobados: {aprobados}")
print(f"Las notas mayores a cinco son: {notasCinco}")



