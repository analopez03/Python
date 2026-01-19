'''Diccionario anidado con alumnos, recorrerlo y si algun alumno tiene menos de 5 se lo actualizamos a 5'''

alumnos = {
    "estud1": {
        "nombre": "Alejandro",
        "Python": 5
    },

    "estud2": {
        "nombre": "Pablo",
        "Python": 7
    },

    "estud3": {
        "nombre": "Sebas",
        "Python": 9
    },

    "estud4": {
        "nombre": "Alberto",
        "Python": 8
    },

    "estud5": {
        "nombre": "David",
        "Python": 3
    },

    "estud6": {
        "nombre": "Alex",
        "Python": 4
    },

    "estud7": {
        "nombre": "Mónica",
        "Python": 7
    },

    "estud8": {
        "nombre": "Franco",
        "Python": 6
    },

    "estud9": {
        "nombre": "Ana",
        "Python": 8
    },

    "estud10": {
        "nombre": "Manuel",
        "Python": 10
    },

    "estud11": {
        "nombre": "Rafael",
        "Python": 9
    },

    "estud12": {
        "nombre": "Carlos",
        "Python": 8
    }
}

for alumno in alumnos.values():
    if alumno["Python"] < 5:
        alumno["Python"] = 5

for alumno, nota in alumnos.items():
    print(alumno, nota)

