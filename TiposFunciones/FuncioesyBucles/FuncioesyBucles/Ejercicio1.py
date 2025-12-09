def calculadora(num1, num2, opc):
    try:
        if opc == "+":
            return num1 + num2
        elif opc == "-":
            return num1 - num2
        elif opc == "*":
            return num1 * num2
        elif opc == "/":
            if num2 == 0:
                return "Error: no se puede dividir entre cero."
            return num1 / num2
        else:
            return "Operación no válida."
    except ValueError:
        return "Error: debes introducir solo números."

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
opc = input("Elige una operación (+, -, *, /) o 'salir' para terminar: ")

print(f"La {opc} de {num1} {opc} {num2} es {calculadora(num1, num2, opc)}")