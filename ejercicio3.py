"""3. Implementar un algoritmo (en una o más funciones) que, dado un número entero n, permita
calcular su factorial."""

def calcularFactorial(n):

    """Calcula el factorial de un numero n"""

    resultado = n
    for i in range(1 , n):

        resultado = resultado * i

    return resultado


print("Calcular el factorial dado un numero: ")
print(calcularFactorial(int(input("Ingrese el numero "))))
