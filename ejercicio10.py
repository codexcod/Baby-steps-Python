import random   
from random import randrange
           
x=(random.randrange(50))

intentos = 0
numero = 0

while not numero == x:
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
   