
def esCpaitalizada(palabra1,palabra2):
    """Compara si la primera palabra es la version capitalizada de la segunda"""
    return palabra1 == palabra2.upper()


print(esCpaitalizada(input("Ingrse la palabra 1 "),input("Ingrese la plabra 2 ")))