"""
8. (Puede ser difícil) Escribir un programa que reciba como entrada un entero representando un
año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en
números romanos.
"""

romanos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def pasarRomano(año):
    """Recibe:
                año:<int>

               Devuelve el año dado en numero romanos"""

    resultado = ""
    while año > 0:
        for n, r in romanos:
            while año > n or año == n:
                resultado = resultado + r
                año = año - n
    return resultado


año=input("Ingrese un año : ")
if (str(año)).isdigit():
    if int(año) < 0:
        "Ingreso un año no valido"
    elif int(año) == 0:
        "No se epuede representar el 0"
    else:
        print(pasarRomano(int(año)))
else:
    print("Ingrese un numero correccto")