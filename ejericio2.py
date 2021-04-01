
def pedirPerimetro():

    print("Calcular el perimetro de un rectangulo")

    perimetro = calcularPerimetro(int(input("Ingrese la base del rectangulo ")),int(input("Ingrese la altura del rectangulo ")))

    print(f"El perimetro de su rectangulo es {perimetro}")

    cargarFunciones()



def calcularPerimetro(base, altura):

    perimetro = base * 2 + altura * 2
    return perimetro

def pedirArea():

    print("Calcular el area de un rectangulo")
    area = calcularArea(int(input("Ingrese la base del rectangulo ")),int(input("Ingrese la altura del rectangulo ")))
    print(f"El area de su rectangulo es {area}")

    cargarFunciones()


def calcularArea(base,altura):

    area = base * altura
    return area


def pedirAreaEjes():
    print("Calcular el area de un rectangulo teniendo en cuenta los ejes x1, x2 , y1 e y2")
    print("ingrese los valores para la coordenada x")
    x1 = int(input("ingrese el valor de x1:"))
    x2 = int(input("ingrese el valor de x2:"))
    print("ingrese los valores para la coordenada y")
    y1 = int(input("ingrese el valor de y1:"))
    y2 = int(input("ingrese el valor de y2:"))
    print(f"El area es {calcularAreaEjes(x1, x2, y1, y2)}")

    cargarFunciones()


def calcularAreaEjes(x1,x2,y1,y2):
    
    base = calcularDistancia(x1,x2)
    altura = calcularDistancia(y1, y2)

    area = base * altura

    return area
    
def calcularDistancia(n1,n2):
    distancia = 0
    if abs(n1)> abs(n2):
        distancia = abs(n1)-abs(n2)
    else:
        distancia = abs(n2)-abs(n1)
    return distancia


def pedirPerimetroCirculo():

    print("Calcular el perimetro de un circulo: ")
    perimetro = calcularPerimetroCirculo(int(input("Inserte el radio del circulo ")))
    print (f"El perimetro es {perimetro}")

    cargarFunciones()

def calcularPerimetroCirculo(radio):    
    diametro = radio * 2
    perimetro = diametro * 3,14
    return perimetro

def pedirAreaCirculo():
    print("Calcular el area de un circulo: ")
    area = calcularAreaCirculo(int(input("Inserte el radio del circulo ")))
    print (f"El area es {area}")

    cargarFunciones()

def calcularAreaCirculo(radio):    
    cuadrado = radio * radio
    area = cuadrado * 3,14
    return area


def pedirVolumenEsfera():
    print("Calcular el volumen de una esfera: ")
    volumen = calcularVolumenEsfera(int(input("Inserte el radio de la esfera ")))
    print (f"El volumen es {volumen}")

    cargarFunciones()

def calcularVolumenEsfera(radio):
    cubo = radio * radio * radio
    volumen = (4/3) * cubo * 3,14
    return volumen


def pedirHipotenusa():
    print("Calcular la hipotenusa dados los catetos 1 y 2: ")
    c1 = int(input("Inserte el cateto numero 1 "))
    c2 = int(input("Inserte el cateto numero 2 "))

    print (f"La hipotenusa es {calcularHipotenusa(c1, c2)}")

    cargarFunciones()

def calcularHipotenusa(c1,c2):
    
    hipotenusa = (c1 ** 2+c2 **2)**(1/2)
    return hipotenusa
 

def cargarFunciones():
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








    

