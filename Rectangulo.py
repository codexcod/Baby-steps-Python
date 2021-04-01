
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

    print("Calcular el perimetro deun circulo: ")
    perimetro = calcularPerimetroCirculo(int(input("Inserte el radio del circulo ")))
    print (f"El perimetro es {perimetro}")

    cargarFunciones()

def calcularPerimetroCirculo(radio):    
    diametro = radio * 2
    perimetro = diametro * 3,14
    return perimetro

def pedirAreaCirculo():
    print("Calcular el area deun circulo: ")
    area = calcularAreaCirculo(int(input("Inserte el radio del circulo ")))
    print (f"El area es {area}")

    cargarFunciones()

def calcularAreaCirculo(radio):    
    cuadrado = radio * radio
    area = cuadrado * 3,14
    return area




def cargarFunciones():
    opcion = int(input("""

    Seleccione la funcion a utilizar:

1.Calcular perimetro
2.Calcular area
3.Calcular area con ejes
4.Calcular perimetro de un circulo
5.Calcular area de un circulo

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

cargarFunciones()








    

