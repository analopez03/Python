def es_primo(n):
    try:
        if n == 1:
            return False

        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1

        return True
    except TypeError:
        return "Error: introduce un número entero válido."


num = int(input("Introduce un número entero positivo: "))
print(f"El número {num} es primo? {es_primo(num)}")