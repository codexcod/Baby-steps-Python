import time
from time import sleep

def validarContraseña(contraseña):
    CONTRASEÑA = "contraseña123@"
    return contraseña == CONTRASEÑA



intentos = 3
espera = 2 

while intentos > 0:

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