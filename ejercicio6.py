"""6. Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de
ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más
grande que se puede obtener entre ellos (8 = −2 × −4) """


def calcularMayorProducto(n1,n2,n3,n4):
    """Recibe:
                   n1:<int>/<float>
                   n2:<int>/<float>
                   n3:<int>/<float>
                   n4:<int>/<float>
               Devuelve el mayor producto entre dos numeros, dados n1, n2 ,n3 y n4"""

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

    return "{0:.2f}".format(mayorProducto)


def pedirNumeros():
    """Pide el ingrso de los 4 numeros"""

    print("Calcular el mayor productos dados 4 numeros")
    resultado = calcularMayorProducto(float(input("Ingrese el primer numero : ")),float(input("Ingrese el segundo numero : ")),float(input("Ingrese el tercer numero : ")),float(input("Ingrese el cuarto numero : ")))
    return (f"El mayor producto es : {resultado}")

