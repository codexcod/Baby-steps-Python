"""13. Escribir un programa que compare dos strings y devuelva True si el primero es la versión
capitalizada del segundo.
Nota: Por ejemplo, la versión capitalizada de la palabra “programar” es
“PROGRAMAR”."""

def esCpaitalizada(palabra1,palabra2):
    """Recibe:
                   palabra1:<str>
                   palabra2:<str>

               Devuelve verdadero o falso dependiendo si la palabra 1 es la version capitalizada de la palabra 2"""
    return palabra1 == palabra2.upper()


print(esCpaitalizada(input("Ingrse la palabra 1 "),input("Ingrese la plabra 2 ")))