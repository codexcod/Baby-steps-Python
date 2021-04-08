def calcularBiciesto(anio):
    if (anio % 4 == 0):
        if(anio % 100 == 0):
            return  anio // 400 == 0
        else:
            return True

    else:
        return False

def pedirBiciesto():

    anio = int(input("Ingrese el año a calcular : "))
    if(calcularBiciesto(anio)):
        print("El año es biciesto")
    else:
        print("El año no es biciesto")