def convertirFarenheitCelsius(grados):
    resultado = (grados-32)/(9/5)
    return resultado


def generarTabla():
    tabla = "Tabla de grados farenheit a celsius  "
    for i in (10,20,30,40,50,60,70,80,90,100,110,120):
        tabla += f"\n {i}F = {convertirFarenheitCelsius(i)}C"

    return tabla


print(generarTabla())