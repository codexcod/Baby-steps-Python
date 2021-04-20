""""17. Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Además elimina todos los
espacios en blanco de más. Por ejemplo, al texto " Llego mañana alrededor del mediodía "
se transcribe como "Llego mañan@ alred@ del medio@". Por otro lado cobra un valor para
las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).

1. Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
telegrama y el costo del mismo.
2. Los puntos se reemplazan por la palabra especial ”STOP”, y el punto final (que puede
faltar en el texto original) se indica como ”STOPSTOP”. Al texto: " Llego mañana
alrededor del mediodía. Voy a almorzar " Se lo transcribe como: "Llego mañan@
alred@ del medio@ STOP Voy a almor@ STOPSTOP"."""


def procesarTelegrama(frase,cantidadMaxima,costoLargo,costoCorto):
    """Procesa un telegrama agragando utilizando los parametros de letrasMaximas y su precio dadas"""
    palabras = frase.split(" ")
    palabras[-1] = palabras[-1].rstrip(".")

    resultado = ""
    total = 0
    for palabra in palabras:
        punto = False

        for letra in palabra:
            if letra == ".":
                palabra = palabra.rstrip(".")
                punto = True



        if len(palabra) >= cantidadMaxima:
            resultado += palabra[0:cantidadMaxima]+"@ "
            total += costoLargo
        else:
            resultado += palabra + " "
            total += costoCorto

        if punto:
            resultado += palabra.replace(palabra, "STOP") + " "





    resultado += "STOPSTOP"
    return f"""El telgrrama es: 
{resultado} 
utilizando {cantidadMaxima} letras maximas por palabra a un costo de ${total} """


