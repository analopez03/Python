def tabla_multiplicar(numero, multiplicador):
    try:
        return numero * multiplicador
    except TypeError:
        return "Error: ambos parámetros deben ser números."

num = int(input("Introduce un número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {tabla_multiplicar(num, i)}")
