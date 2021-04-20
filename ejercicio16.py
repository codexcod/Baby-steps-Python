""""16.
 Escribir funciones que dada una cadena de caracteres:

1. Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
'logaritmos' debe devolver 'lgrtms' .
2. Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
devolver 'i ooae'.
3. Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
devolver 'vistaerou'.
4. Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
(se lee igual de izquierda a derecha que de derecha a izquierda)."""


def mostrarConsonantes(palabra):
    """" de una palabra o frase saca todas las vocales y deja las consonantes"""
    resultado = ""
    for i in palabra:
        if not i in "aeiouAEIOU":
            resultado += i
    return resultado

def mostrarVocales(palabra):
    """" de una palabra o frase saca todas las consonantes y deja las vocales"""
    resultado = ""
    for i in palabra:
        if i in "aeiouAEIOU":
            resultado += i
    return resultado

def moverVocales(palabra):
    """"mueve las vocales una para adelante. Ejemplo: a va a pasar a ser e"""
    vocales = ["a", "e", "i", "o", "u"]
    for letra in palabra:
        if letra in "aeiouAEIOU":
            for i in range (0,4):
                if letra == vocales[i]:
                    palabra = palabra.replace(letra,vocales[i+1])
            if(letra == "u"):
                palabra = palabra.replace(letra, vocales[0])

    return palabra


def esCapicua(palabra):
    """"devuelve true o false dependiendo si es capicua"""
    return  palabra == palabra[::-1]

