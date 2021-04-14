class Vocales:
    """ queria probar como se hace una clase"""
    a = 0
    e=0
    i=0
    o=0
    u=0


palabra = input("Ingrese la palbara para saber cauntas vocales tiene ")

vocales = Vocales()

vocales.a = palabra.count("a")
vocales.e = palabra.count("e")
vocales.i = palabra.count("i")
vocales.o = palabra.count("o")
vocales.u = palabra.count("u")


print(f"""
A:{vocales.a}  
E:{vocales.e}   
O:{vocales.o}
I:{vocales.i}
U:{vocales.u}

""")