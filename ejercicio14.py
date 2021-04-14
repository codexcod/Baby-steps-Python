import random   
from random import randrange

def esValido(numero):
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
    numero = 0
    while not esValido(numero):
        numero = randrange(10000)
    return numero

def compararNumeros(numero1,numero2):
    return str(numero1) == str(numero2)

def pedirNumero(numero):
    while not esValido(numero):
        print("Ingrese un numero valido")
        numero = input("Ingrese un numero ")
    return numero


def jugar():
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