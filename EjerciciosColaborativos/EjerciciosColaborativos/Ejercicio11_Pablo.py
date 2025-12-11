'''Crear una función que reciba un DNI por parámetro y valide si es correcto.
El DNI debe tener 8 números y 1 letra, y la letra debe coincidir con la letra oficial obtenida con la fórmula del DNI (número % 23 usando la cadena "TRWAGMYFPDXBNJZSQVHLCKE").
La función debe devolver True si el DNI es válido y False si no lo es.
Después, probar la función con varios DNIs.'''

def validar_dni(dni):
    letras_oficiales = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if len(dni) != 9:
        return False
    
    numero = dni[:8]
    letra = dni[8].upper()
    
    if not numero.isdigit():
        return False
    
    numero_int = int(numero)
    letra_correcta = letras_oficiales[numero_int % 23]
    
    return letra == letra_correcta

# Probar la función con varios DNIs
dnis_a_probar = ["12345678Z", "87654321X", "1234567A", "12345678A", "00000000T"]
for dni in dnis_a_probar:
    es_valido = validar_dni(dni)
    print(f"DNI: {dni} - Válido: {es_valido}")
    
    