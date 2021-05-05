""" 11. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo
de exámenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por
el alumno, indicando con un valor centinela que no hay más exámenes a revisar. Debe
mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos
respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no """

def calcularNotaMinima(ejercicios, porcentaje):
    """Recibe:
                       ejercicios:<int>
                       porcentaje: <int>/<float>

                   Devuelve la nota minama para aprobar la prueba teniendo en cuenta la cantidad de ejercicios y el porcentaje minimo para aprobar"""
    notaMinima = (porcentaje * ejercicios) / 100
    return notaMinima

def calcularNotaPorcentaje(nota, ejercicios):
    """Recibe:
                           nota:<int>/<float>
                           ejercicios: <int>

                       Devuelve el porcentaje de la prueba aprobado teniendo en cuenta la nota y la cantidad de ejercicios"""
    notaPorcentaje = (nota * 100) / ejercicios
    return notaPorcentaje

def aprobarPureba(cantidadEjercicios,minimoPorcentaje,nota):
    """Recibe:
                               cantidadEjercicios:<int>
                               minimoPorcentaje: <int>/<float>
                               nota:<int>/<float>

                           Devuelve el porcentaje de la prueba aprobado teniendo en cuenta la nota y la cantidad de ejercicios"""

    """Calcula si la prueba esta aprobada o no teniendo en cuenta su nota, el porcentaje necesario para aprobar y la cantidad de ejercicios"""

    while cantidadEjercicios <= 0:
        cantidadEjercicios = int(input("Ingrese la cantidad de ejercicios "))
        if cantidadEjercicios <= 0:
            print("No puede ingresar una cantidad negativa o 0")

    while minimoPorcentaje < 0 or minimoPorcentaje > 100:
        minimoPorcentaje = float(input("Ingrese el porcentaje de ejercicios para aprobar "))
        if cantidadEjercicios <= 0:
            print("Ingrese un porcentaje valido")

    while nota <= 0:
        nota = float(input("Ingrese cuantos ejercicios correctos: "))
        if nota > cantidadEjercicios or nota < 0:
            print("Ingrese una nota valida")

    if nota >= calcularNotaMinima(cantidadEjercicios, minimoPorcentaje):
        return(f"El alumno aprobo con un {calcularNotaPorcentaje(nota, cantidadEjercicios)}% de los ejercicios correctos")
    elif nota < aprobarExamen(cantidadEjercicios, minimoPorcentaje):
        return(f"El alumno reprobo con un {calcularNotaPorcentaje(nota, cantidadEjercicios)}% de los ejercicios correctos")

