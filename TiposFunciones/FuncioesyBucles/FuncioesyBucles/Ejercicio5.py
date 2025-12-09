'''def primos_hasta_n(n):
    try:
        n = int(input("Introduce un número entero positivo: "))
        if n < 2:
            print("Debe ser mayor o igual a 2.")
            return

        print(f"Números primos desde 2 hasta {n}:")
        for num in range(2, N + 1):
            es_primo = True
            divisor = 2
            
            while divisor < num:
                if num % divisor == 0:
                    es_primo = False
                    break
                divisor += 1
                
            if es_primo:
                print(num, end=" ")
        print()
    except ValueError:
        print("Error: introduce un número entero válido.")

primos_hasta_n()'''

def primos_hasta_n(n):
    try:
        if n < 2:
            return []

        primos = []
        for num in range(2, n + 1):
            es_primo = True
            divisor = 2
            while divisor < num:
                if num % divisor == 0:
                    es_primo = False
                    break
                divisor += 1
            if es_primo:
                primos.append(num)
        return primos
    except TypeError:
        return "Error: introduce un número entero válido."

n = int(input("Introduce un número entero positivo: "))
print(f"Los números primos hasta {n} son: {primos_hasta_n(n)}")
