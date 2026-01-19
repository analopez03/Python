'''Ejercicio 2
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable.
Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes. coger datos de otro diccionario'''


def creacion_personaje():
    estadistica_base = 2

    caballero = {
        "vida": estadistica_base * 2,
        "defensa": estadistica_base * 2,
        "alcance": estadistica_base,
        "ataque": estadistica_base
    }

    guerrero = {
        "vida": caballero["vida"] / 2,
        "defensa": caballero["defensa"] / 2,
        "alcance": caballero["alcance"] * 2,
        "ataque": caballero["ataque"] * 2
    }

    arquero = {
        "vida": guerrero["vida"],
        "defensa": guerrero["defensa"] / 2,
        "alcance": guerrero["alcance"] * 2,
        "ataque": guerrero["ataque"]
    }

    return caballero, guerrero, arquero

caballero, guerrero, arquero = creacion_personaje()
print("Estadisticas del caballero", caballero)
print("Estadisticas del guerrero", guerrero)
print("Estadisticas del arquero", arquero)


