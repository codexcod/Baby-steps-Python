
def pedirPerimetro():

    print("Calcular el perimetro de un rectangulo")

    perimetro = calcularPerimetro(int(input("Ingrese la base del rectangulo ")),int(input("Ingrese la altura del rectangulo ")))

    print(f"El perimetro de su rectangulo es {perimetro}")



def calcularPerimetro(base, altura):

    perimetro = base * 2 + altura * 2
    return perimetro

def pedirArea():

    print("Calcular el area de un rectangulo")
    area = calcularArea(int(input("Ingrese la base del rectangulo ")),int(input("Ingrese la altura del rectangulo ")))
    print(f"El area de su rectangulo es {area}")


def calcularArea(base,altura):

    area = base * altura
    return area


pedirArea()
#pedirPerimetro()


    

