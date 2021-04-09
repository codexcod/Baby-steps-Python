def calcularBiciesto(anio):
    if (anio % 4 == 0):
        if(anio % 100 == 0):
            return  anio // 400 == 0
        else:
            return True

    else:
        return False

def cantidadDiasMes(mes):

    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    if isinstance(mes, int):
        return dias[mes - 1]
    else:
        for i in range(0,12):
            if meses[i] == mes:
                return dias[i]


def esValido(dia,mes,año):
    return mes >= 0 and mes <= 12 and dia >= 0 and dia <= cantidadDiasMes(mes)

def cuantosDiasFaltanMes(dia,mes,año):
    if (esValido(dia,mes,año)):
        return cantidadDiasMes(mes)-dia
    else:
        return "La fecha no es valida"

def cuantosDiasFaltanAño(dia,mes,año):
    if (esValido(dia,mes,año)):
        dias = cuantosDiasFaltanMes(dia, mes, año)
        for i in range(mes,12):
            dias += cantidadDiasMes(i)
        return dias

    else:
        return "La fecha no es valida"


def cuantosDiasVanAño(dia,mes,año):
    if (esValido(dia,mes,año)):
        dias = dia
        for i in range(0,mes-1):
            dias += cantidadDiasMes(i)
        return dias

    else:
        return "La fecha no es valida"

def distancianEntreDosFechas(dia1,mes1,año1,dia2,mes2,año2):
    if esValido(dia1,mes1,año1) and esValido(dia2,mes2,año2):

        if año1 > año2:
            diferenciaAño =año1-año2
            diferenciaMes = mes1-mes2-1
            diferenciaDia = cuantosDiasFaltanMes(dia2,mes2,año2) + dia1

            diferenciaAño -= 1
            diferenciaMes = 12 - abs(diferenciaMes)

            while diferenciaMes >= 12 :
                    diferenciaAño += 1
                    diferenciaMes -=12



            while diferenciaDia > 31 :
                    diferenciaMes += 1
                    diferenciaDia -=31


        return f"{diferenciaDia} / {diferenciaMes} / {diferenciaAño}"



print(distancianEntreDosFechas(24,4,2021,22,8,2004))

