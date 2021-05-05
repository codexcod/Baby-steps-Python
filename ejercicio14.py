import random   
from random import randrange

"""14. Mastermind: Cada vez que se empieza un partido, el programa debe “eligir” un número de
cuatro cifras (sin cifras repetidas), que será el código que el jugador debe adivinar en la
menor cantidad de intentos posibles. Cada intento consiste en una propuesta de un código
posible que tipea el jugador, y una respuesta del programa. Las respuestas le darán pistas al
jugador para que pueda deducir el código.
Estas pistas indican cuán cerca estuvo el número propuesto de la solución a través de dos
valores: la cantidad de aciertos es la cantidad de dígitos que propuso el jugador que también
están en el código en la misma posición. La cantidad de coincidencias es la cantidad de
digitos que propuso el jugador que también están en el código pero en una posición distinta.
Por ejemplo, si el código que eligió el programa es el 2607, y el jugador propone el 1406, el
programa le debe responder un acierto (el 0, que está en el código original en el mismo
lugar, el tercero), y una coincidencia (el 6, que también está en el código original, pero en la
segunda posición, no en el cuarto como fue propuesto). Si el jugador hubiera propuesto el
3591, habría obtenido como respuesta ningún acierto y ninguna coincidencia, ya que no hay
números en común con el código original, y si se obtienen cuatro aciertos es porque el
jugador adivinó el código y ganó el juego.
El programa, entonces, debe generar un número que el jugador no pueda predecir. A
continuación, debe pedirle al usuario que introduzca un número de cuatro cifras distintas, y
cuando éste lo ingresa, procesar la propuesta y evaluar el número de aciertos y de
coincidencias que tiene de acuerdo al código elegido. Si es el código original, se termina el
programa con un mensaje de felicitación. En caso contrario, se informa al jugador la
cantidad de aciertos y la de coincidencias, y se le pide una nueva propuesta. Este proceso se
repite hasta que el jugador adivine el código."""

def esValido(numero):
    """Recibe:
                   numero:<int>

               Devuelve verdadero o falso dependiendo si el numero tiene el formato correcto"""
    n = str(numero)
    if n.isdigit():   
        
        if(len(n) == 4):

            return(n[0:1] != n[1:2] 
            and n[0:1] != n[2:3] 
            and n[0:1] != n[3:4] 
            and n[1:2] != n[2:3] 
            and n[1:2] != n[3:4] 
            and n[2:3] != n[3:4])
            
        else:
            return False
    else:
        return False

def generarNumero():
    """Genera un numero de 4 cifras en el que no se repitan numeros"""
    numero = 0
    while not esValido(numero):
        numero = randrange(10000)
    return numero

def compararNumeros(numero1,numero2):
    """Recibe:
                       numero1:<int>
                       numero2:<int>

                   Devuelve si el numero uno es igual al segundo"""
    return str(numero1) == str(numero2)

def pedirNumero(numero):
    """Recibe:
                         numero1:<int>


                     Pide un numero hasta que se ingrese uno valido"""
    while not esValido(numero):
        print("Ingrese un numero valido")
        numero = input("Ingrese un numero ")
    return numero


def jugar():
    """Printea el juego utilizando todas las funciones"""
    generado = generarNumero()
    print("Comezo el juego")

    numero = pedirNumero(input("Ingrese un numero "))

    while not compararNumeros(numero,generado):
        aciertos = 0
        coincidencias = 0
        
        n= str(numero)
        g= str(generado)
        for i in range(1,5):
            
            if(n[i-1:i] == g[i-1:i]):
                aciertos +=1


        for i in range(1,5):
            
            if(n[i-1:i] == g[1:2] or n[i-1:i] == g[2:3] or n[i-1:i] == g[3:4]):
                coincidencias +=1

        print(f"""No acerto
        
        Aciertos ={aciertos}
        Coincidencias ={coincidencias}
        
        """)
        print(g)
        numero = pedirNumero(input("Ingrese un numero "))


        print("Gano el juego!")

jugar()