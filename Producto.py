"""1. Escribir un programa que pregunte al usuario:
2. Dos números, y luego muestre el producto."""

def producto(num1,num2):
    """Recibe:
            num1: <int>/<float>
            num2: <int>/<float>
        Devuelve el producto entre los dos numeros dados"""

    return "{0:.2f}".format(num1 * num2)


numero1 = float((input("Ingrese un primer numero ")))
numero2 = float((input("Ingrese un segundo numero ")))

print(f"El producto de los dos numero es: {producto(numero1,numero2)}")


    

