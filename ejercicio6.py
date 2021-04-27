"""6. Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de
ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más
grande que se puede obtener entre ellos (8 = −2 × −4) """


def calcularMayorProducto(n1,n2,n3,n4):
    """Dados 4 numeros devuelve el mayor prducto entre 2 de esos numeros"""

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
    """Funcion que printea la funcion anterior"""

    print("Calcular el mayor productos dados 4 numeros")
    resultado = calcularMayorProducto(int(input("Ingrese el primer numero : ")),int(input("Ingrese el segundo numero : ")),int(input("Ingrese el tercer numero : ")),int(input("Ingrese el cuarto numero : ")))
    print(f"El mayor producto es : {resultado}")


