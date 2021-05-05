"""2. Implementar algoritmos (en forma de función) que permitan:
1. Calcular el perímetro de un rectángulo dada su base y su altura.
2. Calcular el área de un rectángulo dada su base y su altura.
3. Calcular el área de un rectángulo (alineado con los ejes x e y ) dadas sus coordenadas
x1,x2, y1,y2.
4. Calcular el perímetro de un círculo dado su radio.
5. Calcular el área de un círculo dado su radio.
6. Calcular el volumen de una esfera dado su radio.
7. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""


def pedirPerimetro():
    """Pide el perimetro de un rectangulo"""

    print("Calcular el perimetro de un rectangulo")

    perimetro = calcularPerimetro(float(input("Ingrese la base del rectangulo ")),float(input("Ingrese la altura del rectangulo ")))

    print(f"El perimetro de su rectangulo es {perimetro}")

    cargarFunciones()



def calcularPerimetro(base, altura):
    """Recibe:
            base:<int>/<float>
            altura:<int>/<float>
        Devuelve el perimetro de un rectangulo teniendo en cuenta su base y altura"""

    perimetro = base * 2 + altura * 2
    return "{0:.2f}".format(perimetro)


def pedirArea():
    """Pide el area de un rectangulo"""

    print("Calcular el area de un rectangulo")
    area = calcularArea(float(input("Ingrese la base del rectangulo ")),float(input("Ingrese la altura del rectangulo ")))
    print(f"El area de su rectangulo es {area}")

    cargarFunciones()


def calcularArea(base,altura):
    """Recibe:
                base:<int>/<float>
                altura:<int>/<float>
            Devuelve el area de un rectangulo teniendo en cuenta su base y altura"""

    area = base * altura
    return "{0:.2f}".format(area)


def pedirAreaEjes():
    """Pide el area de un rectangulo teniendo en cunta 4 ejes"""

    print("Calcular el area de un rectangulo teniendo en cuenta los ejes x1, x2 , y1 e y2")
    print("ingrese los valores para la coordenada x")
    x1 = float(input("ingrese el valor de x1: "))
    x2 = float(input("ingrese el valor de x2: "))
    print("ingrese los valores para la coordenada y")
    y1 = float(input("ingrese el valor de y1: "))
    y2 = float(input("ingrese el valor de y2: "))
    print(f"El area es {calcularAreaEjes(x1, x2, y1, y2)}")

    cargarFunciones()


def calcularAreaEjes(x1,x2,y1,y2):
    """Recibe:
                x1:<int>/<float>
                x2:<int>/<float>
                y1:<int>/<float>
                y2:<int>/<float>
            Devuelve el area de un rectangulo dados los ejes x1 y x2 y y1 y y2"""
    base = calcularDistancia(x1,x2)
    altura = calcularDistancia(y1, y2)

    area = base * altura

    return "{0:.2f}".format(area)
    
def calcularDistancia(n1,n2):
    """Recibe:
                    n1:<int>/<float>
                    n2:<int>/<float>
                Devuelve la distancia entre los puntos n1 y n2"""

    distancia = 0
    if abs(n1)> abs(n2):
        distancia = abs(n1)-abs(n2)
    else:
        distancia = abs(n2)-abs(n1)
    return distancia


def pedirPerimetroCirculo():

    """ Pide el perimetro de un circulo"""

    print("Calcular el perimetro de un circulo: ")
    perimetro = calcularPerimetroCirculo(float(input("Inserte el radio del circulo ")))
    print (f"El perimetro es {perimetro}")

    cargarFunciones()

def calcularPerimetroCirculo(radio):
    """Recibe:
                    radio:<int>/<float>
            Devuelve el perimetro de un circulo teniendo en cuenta su radio"""

    diametro = radio * 2
    perimetro = diametro * 3,14
    return (perimetro)

def pedirAreaCirculo():

    """Pide el area de un circulo"""

    print("Calcular el area de un circulo: ")
    area = calcularAreaCirculo(float(input("Inserte el radio del circulo ")))
    print (f"El area es {area}")

    cargarFunciones()

def calcularAreaCirculo(radio):
    """Recibe:
                        radio:<int>/<float>
                Devuelve el area de un circulo teniendo en cuenta su radio"""

    cuadrado = radio * radio
    area = cuadrado * 3,14
    return (area)


def pedirVolumenEsfera():

    """Pide el volumen de una esfera"""

    print("Calcular el volumen de una esfera: ")
    volumen = calcularVolumenEsfera(float(input("Inserte el radio de la esfera ")))
    print (f"El volumen es {volumen}")

    cargarFunciones()


def calcularVolumenEsfera(radio):
    """Recibe:
                        radio:<int>/<float>
                Devuelve el volumen de una esfera teniendo en cuenta su radio"""

    cubo = radio * radio * radio
    volumen = (4/3) * cubo * 3,14
    return "{0:.2f}".format(volumen)


def pedirHipotenusa():

    """Pide la hipotenusa dados sus dos catetos"""

    print("Calcular la hipotenusa dados los catetos 1 y 2: ")
    c1 = float(input("Inserte el cateto numero 1 "))
    c2 = float(input("Inserte el cateto numero 2 "))

    print (f"La hipotenusa es {calcularHipotenusa(c1, c2)}")

    cargarFunciones()


def calcularHipotenusa(c1,c2):
    """Recibe:
                        c1:<int>/<float>
                        c2:<int>/<float>
                Devuelve la hipotenusa teniendo en cuenta sus catetos"""

    hipotenusa = (c1 ** 2+c2 **2)**(1/2)
    return "{0:.2f}".format(hipotenusa)
 

def cargarFunciones():
    """Funcion que funciona como menu para llamar las demas funciones"""

    opcion = int(input("""
    Seleccione la funcion a utilizar:

1.Calcular perimetro
2.Calcular area
3.Calcular area con ejes
4.Calcular perimetro de un circulo
5.Calcular area de un circulo
6.Calcular volumen de una esfera
7.Calcular la hipotenusa teniendo en cuenta 2 catetos 


"""))
    if opcion == 1:
        pedirPerimetro()
    elif opcion == 2:
        pedirArea()
    elif opcion == 3:
        pedirAreaEjes()
    elif opcion ==4:
        pedirPerimetroCirculo()
    elif opcion ==5:
        pedirAreaCirculo()
    elif opcion ==6:
        pedirVolumenEsfera()
    elif opcion ==7:
        pedirHipotenusa()()


cargarFunciones()








    

