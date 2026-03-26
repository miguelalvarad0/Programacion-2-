

def es_seguro(tablero, fila, col):
    for i in range(fila):
        #print()
        #print (i)
        #print ("tablero[i] == col", tablero[i], ' ==', col, tablero[i] == col)
        #print ("tablero[i] - i == col - fila", tablero[i], "-", i, "==", col, "-", fila, tablero[i] - i == col - fila)
        #print ("tablero[i] + i == col + fila", tablero[i], "+", i, "==", col, "+", fila, tablero[i] + i == col + fila)
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

solucion = 1
def resolver_reinas(tablero, fila):
    global solucion
    if fila == len(tablero):
        #print('Solucion:', solucion)
        solucion += 1
        print(tablero)
        imprimir_tablero(tablero)
        return

    for col in range(8):
        if es_seguro(tablero, fila, col):
            tablero[fila] = col
            print('Sí seguro:', fila,',', col, '>',tablero)
            resolver_reinas(tablero, fila + 1)
            tablero[fila] = -1  # backtrack
        #else:
            #print('No seguro:', fila,',', col, '>',tablero)

def imprimir_tablero(tablero):
    for i in range(8):
        fila = ["."] * 8
        fila[tablero[i]] = "Q"
        print(" ".join(fila))
    print()




'''
. . . . . . . Q
. . . Q . . . .
Q . . . . . . .
. . Q . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . Q .
. . . . Q . . .
'''

# Inicia con todas las posiciones vacías
tablero = [-1] * 8  #
resolver_reinas(tablero, 0)
