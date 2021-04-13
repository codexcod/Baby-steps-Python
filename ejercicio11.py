def calcularNotaMinima(ejercicios, porcentaje):
    """Calcula la nota minama para aprobar la prueba teniendo en cuenta la cantidad de ejercicios y el porcentaje minimo para aprobar"""
    notaMinima = (porcentaje * ejercicios) / 100
    return notaMinima

def calcularNotaPorcentaje(nota, ejercicios):
    """Calcula el porcentaje de la prueba aprobado teniendo en cuenta la nota y la cantidad de ejercicios"""
    notaPorcentaje = (nota * 100) / ejercicios
    return notaPorcentaje

def aprobarPureba(cantidad_ejercicios,minimo_porcentaje,nota):
    """Calcula si la prueba esta aprobada o no teniendo en cuenta su nota, el porcentaje necesario para aprobar y la cantidad de ejercicios"""

    while cantidad_ejercicios <= 0:
        cantidad_ejercicios = int(input("Ingrese la cantidad de ejercicios "))
        if cantidad_ejercicios <= 0:
            print("No puede ingresar una cantidad negativa o 0")

    while minimo_porcentaje < 0 or minimo_porcentaje > 100:
        minimo_porcentaje = int(input("Ingrese el porcentaje de ejercicios "))
        if cantidad_ejercicios <= 0:
            print("Ingrese un porcentaje valido")

    while nota <= 0:
        nota = int(input("Ingrese cuantos ejercicios correctos: "))
        if nota > cantidad_ejercicios or nota < 0:
            print("Ingrese una nota valida")

    if nota >= calcularNotaMinima(cantidad_ejercicios, minimo_porcentaje):
        print(f"El alumno aprobo con un {calcularNotaPorcentaje(nota, cantidad_ejercicios)}% de los ejercicios correctos")
    elif nota < aprobarExamen(cantidad_ejercicios, minimo_porcentaje):
        print(f"El alumno reprobo con un {calcularNotaPorcentaje(nota, cantidad_ejercicios)}% de los ejercicios correctos")

