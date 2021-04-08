def calcularMayorProducto(n1,n2,n3,n4):
    mayorProducto = 0

    for i in (n2,n3,n4):
        producto = n1 * i
        if(producto > mayorProducto):
            mayorProducto = producto
    for i in (n3, n4):
        producto = n2 * i
        if (producto > mayorProducto):
            mayorProducto = producto

    producto = n3 * n4
    if (producto > mayorProducto):
        mayorProducto = producto

    return (mayorProducto)


def pedirNumeros():
    print("Calcular el mayor productos dados 4 numeros")
    resultado = calcularMayorProducto(int(input("Ingrese el primer numero : ")),int(input("Ingrese el segundo numero : ")),int(input("Ingrese el tercer numero : ")),int(input("Ingrese el cuarto numero : ")))
    print(f"El mayor producto es : {resultado}")

pedirNumeros()
