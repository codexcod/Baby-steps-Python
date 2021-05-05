"""15. Escribir una función que dada una cadena de caracteres, devuelva:
1. La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
devolver 'USB'.
2. Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.

3. Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe
devolver 'Antes ayer'"""

def mostrarSiglasDeCadena(cadena):
    """Recibe:
                cadena:<string>

                Devuelve una cadena de texto en siglas usando las primeras letras"""
    palabras = cadena.split(" ")
    resultado=""

    for palabra in palabras:
        resultado += palabra[0]

    return resultado.upper()


def mostrarMayusculaAlPrimero(cadena):
    """Recibe:
                cadena:<string>

                Devuelve la cadena conviertiendo a todas las primeras letras de cada palabra en mayuscula"""
    palabras = cadena.split(" ")

    resultado = ""

    for palabra in palabras:

        resultado += palabra.capitalize() + " "

    return resultado


def mostrarPalabrasConA(cadena):
    """Recibe:
                cadena:<string>

                Devuelve una cadena mostrando las palabras de la cadena que empiezen con a"""
    palabras = cadena.split(" ")

    resultado = ""

    for palabra in palabras:

        if palabra[0] == "a" or palabra[0] == "A":
            resultado += palabra + " "

    if resultado == "":

        resultado=f"No hay palabras con la letra a"

    return resultado





