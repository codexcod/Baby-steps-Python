import time
from time import sleep
""" 9. Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la
contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
1. Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
2. Modificar el programa anterior para que después de cada intento agregue una pausa cada
vez mayor, utilizando la función sleep del módulo time.
3. Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False). """

def validarContraseña(contraseña):
    """Recibe:
                   contraseña:<str>

               Devuelve si verdadero o falso dependiendo si la contraseña es correcta o no"""
    return contraseña == "contraseña123@"



intentos = 3
espera = 2 

while intentos > 0:
    """Mientras el jugador tenga intentos puede ingresar una contraseña"""

    contraseña_ingresada = input("Ingrese la contraseña ")

    if(validarContraseña(contraseña_ingresada)):
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        intentos -= 1
        if(intentos == 0):
            print("Se le acabaron los intentos")
            break 
        else:
            print(f"le quedan {intentos} intentos")
            time.sleep(espera)
            espera +=1