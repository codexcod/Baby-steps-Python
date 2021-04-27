import random   
from random import randrange

"""10. Utilizando la función randrange del módulo random, escribir un programa que tenga un
número aleatorio secreto, y luego permita al usuario ingresar números y le indique si son
menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
correcto. """
           
x=(random.randrange(50))

intentos = 0
numero = 0

while not numero == x:
    """Mientras el numero no sea correco el jugador puede seguir intentando"""

    numero = int(input("Ingrese un numero"))
    
    if numero > x:
        intentos += 1
        print("El numero es mas chico")

    elif numero < x:
        intentos += 1
        print ("El numero es mas grande")
        
    elif numero == x:
        print(f"El numero es correcto, acertaste en el intento {intentos}")
        intentos = 0
        break
   