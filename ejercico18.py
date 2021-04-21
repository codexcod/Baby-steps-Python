"""18. Inversión de listas
1. Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá
devolver ['papa', 'a', 'día', 'buen', 'Di'].
2. Realizar otra función que invierta la lista, pero en lugar de devolver una nueva,
modifique la lista dada para invertirla, sin usar listas auxiliares"""

def invertirListaConAuxiliar(lista):
    """Dada una lista devuelve una nueva lista com la primera lista invertida"""
    resultado = []
    for i in range(len(lista)-1,-1,-1):
        resultado.append(lista[i])
    return resultado

def invertirLista(lista):
    """Dada una lista devuelve la lista invertida"""
    cantidad = len(lista)
    for i in range(cantidad):
        lista.append(lista[cantidad-i-1])
        lista.remove(lista[cantidad-i-1])
        
    return lista



