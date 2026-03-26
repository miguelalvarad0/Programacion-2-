def atomo(x):
    return not type(x) == list
def raiz (arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

def hijoizq (arbol):
    if atomo(arbol):
        return []
    else: return arbol[1]

def hijoder (arbol):
    if atomo(arbol):
        return []
    else: return arbol[2]

def lista_hojas(arbol):
    if arbol == []:
        return []

    if atomo(arbol):
        return [arbol]

    if hijoizq(arbol) == [] and hijoder(arbol) == []:
        return [raiz(arbol)]

    return lista_hojas(hijoizq(arbol)) + lista_hojas(hijoder(arbol))

a = [20,[10,5,6],90]
print(lista_hojas(a))