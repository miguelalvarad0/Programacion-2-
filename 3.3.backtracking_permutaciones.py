
def permutar(lista, camino=[]):
    if lista == []:   #not lista  
        print(camino)
        return

    #print()
    for i in range(len(lista)): # len 1 - n
        # Elegimos el elemento i
        nuevo_elemento = lista[i]
        # Generamos una nueva lista sin ese elemento
        resto = lista[:i] + lista[i+1:]
        print('lista entrada:',lista, 'camino entrada:',camino, i,':',nuevo_elemento, 'lista:', resto, camino + [nuevo_elemento])
        # Exploramos con esa nueva elección
        permutar(resto, camino + [nuevo_elemento])

# Ejemplo:
permutar(['A', 'B', 'C'])

