"""7. Escribir funciones que resuelvan los siguientes problemas:

1. Dado un año indicar si es bisiesto. (Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
2. Dado un mes, devolver la cantidad de días correspondientes.
3. Dada una fecha (día, mes, año), indicar si es válida o no.
4. Dada una fecha, indicar los días que faltan hasta fin de mes.
5. Dada una fecha, indicar los días que faltan hasta fin de año.
6. Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
7. Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días."""

def calcularBiciesto(anio):
    """Caclula si un año es biciesto"""
    if (anio % 4 == 0):
        if(anio % 100 == 0):
            return  anio // 400 == 0
        else:
            return True

    else:
        return False

def cantidadDiasMes(mes,año):
    """Caclcula la cantidad de dias que tiene un mes y tiene en cuenta si es biciesto"""
    dias = []
    if(calcularBiciesto(año)):
        dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    else:
        dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    if isinstance(mes, int):
        return dias[mes - 1]
    else:
        for i in range(0,12):
            if meses[i] == mes:
                return dias[i]


def esValido(dia,mes,año):
    """Devuelve True or False dependiendo si la fecha es valida"""
    return mes >= 0 and mes <= 12 and dia >= 0 and dia <= cantidadDiasMes(mes,año)

def cuantosDiasFaltanMes(dia,mes,año):
    """Calcula la cantidad de dias que faltan para terminar el mes"""
    if (esValido(dia,mes,año)):
        return cantidadDiasMes(mes,año)-dia
    else:
        return "La fecha no es valida"

def cuantosDiasFaltanAño(dia,mes,año):
    """Caclula la cantidad de dias que faltan para terminar el año"""
    if (esValido(dia,mes,año)):
        dias = cuantosDiasFaltanMes(dia, mes, año)
        for i in range(mes,12):
            dias += cantidadDiasMes(i)
        return dias

    else:
        return "La fecha no es valida"


def cuantosDiasVanAño(dia,mes,año):
    """Caclula la cantidad de dias que pasaron en el año"""
    if (esValido(dia,mes,año)):
        dias = dia
        for i in range(0,mes-1):
            dias += cantidadDiasMes(i,año)
        return dias

    else:
        return "La fecha no es valida"

def distancianEntreDosFechas(dia1,mes1,año1,dia2,mes2,año2):
    """Calcula la distancia entre dos fechas y la devuelve en dias, meses y años"""

    if esValido(dia1,mes1,año1) and esValido(dia2,mes2,año2):

        if año1 < año2:
            dia = 0
            if (dia1 > dia2):
                dia = dia1 - dia2
            elif (dia2 > dia1):
                dia = dia2 - dia1
            elif (dia2 == dia1):
                dia = 0

            mes = mes2 - mes1

            año = año2 - año1

            if mes < 0:
                año -= 1
                mes = 12 + mes

            if dia < 0:
                mes -= 1
                dia = cantidadDiasMes(mes, año) + dia

            resultado = f"{año} Años, {mes} meses y {dia} dias"
            return resultado

        elif año1 > año2:
            año = año1 - año2
            mes = mes1 - mes2

            dia = 0
            if(dia1 > dia2):
                dia = dia1 - dia2
            elif(dia2 > dia1):
                dia = dia2 - dia1
            elif (dia2 == dia1):
                dia = 0


            if mes < 0:
                año -= 1
                mes = 12 + mes

            if dia < 0:
                mes -= 1
                dia = cantidadDiasMes(mes, año) + dia

            resultado = f"{año} Años, {mes} meses y {dia} dias"
            return resultado

        elif año1 == año2:
            año = año1
            if mes1 > mes2:
                mes = mes1 - mes2
                dia = dia1 - dia2
                if dia < 0:
                    mes -= 1
                    dia = cantidadDiasMes(mes1 - mesc2, año) + dia

                resultado = f"la diferencia es de {mes} Meses y {dia} dias"
                return resultado

            elif mes2 > mes1:

                mes = mes2 - mes1
                dia = dia2 - dia1

                if dia < 0:
                    mes -= 1
                    dia = cantidadDiasMes(mes2 - mes1, año) + dia

                diferencia = f"{mes} Meses y {dia} dias"
                return diferencia

            elif mes1 == mes2:

                if dia1 > dia2:
                    dia = dia1 - dia2
                    resultado = f"la diferencia es de {dia} Dias"
                    return resultado

                elif dia2 > dia1:
                    dia = dia2 - dia1
                    resultado = f"la diferencia es de {dia} Dias"
                    return resultado

                elif dia1 == dia2:
                    resultado = "no hay diferencia entre las fechas"
                    return resultado





