
def mostrarSiglasDeCadena(cadena):
    palabras = cadena.split(" ")
    resultado=""

    for palabra in palabras:
        resultado += palabra[0]

    return resultado.upper()

def mostrarMayusculaAlPrimero(cadena):
    palabras = cadena.split(" ")

    resultado = ""

    for palabra in palabras:

        resultado += palabra.capitalize() + " "

    return resultado

def mostrarPalabrasConA(cadena):
    palabras = cadena.split(" ")

    resultado = ""

    for palabra in palabras:

        if palabra[0] == "a" or palabra[0] == "A":
            resultado += palabra + " "

    if resultado == "":

        resultado=f"No hay palabras con la letra a"

    return resultado

print(mostrarSiglasDeCadena("ayer nomas ayer hola algo"))



