"""4. Escribir un programa (con al menos una función) que convierta un valor dado en grados
Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 C + 32.

5. Utilice el programa anterior para generar (imprimir en pantalla) una tabla de conversión de
temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
Nota: La forma ideal es haber implementado en el ejercicio anterior una función para
hacer la traducción entre Fahrenheit y Celcius. En este ejercicio, lo que resta es crear,
para este ejercicio, una función que llame a la anterior varias veces.
"""


def convertirFarenheitCelsius(grados):
    """Recibe:
                   grados:<int>
               Devuelve la cantidad de grados farenheit en celcius"""
    resultado = (grados-32)/(9/5)
    return "{0:.2f}".format(resultado)


def generarTabla():
    """Genera una tabla de valores de Farenheit a celcius de 10 a 120"""
    tabla = "Tabla de grados farenheit a celsius  "
    for i in (10,20,30,40,50,60,70,80,90,100,110,120):
        tabla += f"\n {i}F = {convertirFarenheitCelsius(i)}C"

    return tabla

print(generarTabla())
