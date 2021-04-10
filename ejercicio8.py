

romanos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def pasarRomano(año):
 # Convierte el año ingresado en numeros romanos
    resultado = ""

    while año > 0:
        for n, r in romanos:
            while año > n or año == n:
                resultado = resultado + r
                año = año - n
    return resultado

año=int(input("Ingrese un año : "))
if año < 0:
    "Ingreso un año no valido"
elif año == 0:
    "No se epuede representar el 0"
else: 
    print(pasarRomano(año))