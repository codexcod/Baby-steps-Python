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
    resultado = ""
    for i in palabra:
        if not i in "aeiouAEIOU":
            resultado += i
    return resultado

def mostrarVocales(palabra):
    resultado = ""
    for i in palabra:
        if i in "aeiouAEIOU":
            resultado += i
    return resultado

print(mostrarVocales("sin consonantes"))