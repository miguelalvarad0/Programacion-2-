




##############################
#arboles
# estructura jerarquica sobre un conjunto de objetos llamados nodos
# Los conectores de esa jerarquia se llaman ramas
# Existe un nodo especial, llamado RAIZ
# Un nodo puede ser cualquier tipo de objeto

# Un arbol se puede definir recursivamente:
# el arbol nulo es un arbol
# existe un nodo especial llamado raiz
# los nodos restantes se parte en subconjuntos T1, T2 ... Tn, cada
# uno con una raiz es un subarbol y tiene una raiz

# ARBOL BINARIO
# Nodo Padre, hijo izquierdo, hijo derecho
# mostrar c'omo se representa un arbol con listas

a1 = [10, [5, [2, 1, [3,[],4]], []], [30,25,[60,[50, [40,31,[]],55],[]]]]


# construir un arbol
# centro, hi, hd: arboles binarios
def arbol (centro, hijoizquierdo, hijoderecho):
    if hijoizquierdo == [] and hijoderecho == []:
        return centro
    else:
        return [centro] + [hijoizquierdo] + [hijoderecho]

# funciones que retonan raiz, hi, hd

#atomo
#E: un arbol
#S: booleano
# funcion que indica si es un valor o un subarbol
def atomo(x):
   # return not isinstance (x, list)
    return not type(x) == list

# funcion que retorna la raiz, retorna un valor
#E: arbol
#R: la raiz como un numero
def raiz (arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

# funcion que retorna el hijo izquierdo, retorna un arbol
# E: arbol
# S: retorna el hijo izuqierdo
def hijoizq (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[1]

# funcion que retorna el hijo izquierdo, retorna un arbol
def hijoder (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[2]

# hoja, es cuando no tiene hijos un nodo
# E: recibe un arbol
# S: retorna True si no tiene hijos
def hoja(nodo):
    if nodo == []:
        return False
    elif atomo(nodo):
        return True #[10,[],[]]
    elif hijoizq(nodo) == [] and hijoder(nodo) == []:
        return True
    else:
        return False




#retorna la cantidad de elementos o nodos que tiene un AB
#E: arbol
#S: numero (+ - * / // ...)

def contar_nodos (arbol):
    if arbol == []:
        return 0
    elif hoja(arbol):
        return 1
    #haga algo con la raiz y recursivamente con los hijos el mismo problema
    else:
        return 1 + contar_nodos (hijoizq(arbol)) + contar_nodos (hijoder(arbol))


#retorne la sumatoria de todas llaves de los nodos del arbol
# E: arbol
# S: numero (sumatoria)
def sumatoria(arbol):
    if arbol == []:
        return 0
    else:
        return raiz(arbol) + sumatoria(hijoizq(arbol)) + sumatoria(hijoder(arbol))


#retorne la sumatoria de las claves pares de un árbol binario
#E: arbol
#S: numero
def suma_pares(arbol):
    if arbol == []:
        return 0
    elif raiz(arbol) % 2 == 0:
        return raiz(arbol) + suma_pares(hijoizq(arbol)) + suma_pares(hijoder(arbol))
    else:
        return suma_pares(hijoizq(arbol)) + suma_pares(hijoder(arbol))


#retorne True si todas las claves del AB son pares o cero, False en otro caso
#E: arbol
#S: boolean
def todos_pares(arbol):
    if arbol == []:
        return True
    elif raiz(arbol) % 2 == 1: #es impar
        return False
    else:
        return todos_pares(hijoizq(arbol)) and todos_pares(hijoder(arbol))







# insertar
#inserta en un ABB
def insertar (ele, arb):
    print (ele, arb)
    if arb == []:
        return ele
    elif ele <= raiz(arb):
        return arbol (raiz(arb), insertar(ele, hijoizq(arb)),
                      hijoder(arb))
    else:
        return arbol (raiz(arb), hijoizq(arb), insertar(ele,hijoder(arb)))


# borrar: borra en un ABB, donde atiende 3 casos.
# caso1: borrar un nodo sin hijos, se borra simplemente
# caso2: borrar un nodo con 1 hijo, el hijo lo sustituye
# caso3: sustituirlo por el mayor de los menores o el menor de los mayores

a = [1, [3,5,2], [12,11,[14,13,15]]]

# funcion mayor de un arbol ABB: busca a la derecha el elemento sin hijo derecho
def mayor(arbol):
    if hijoder(arbol) == []:
        return raiz(arbol)
    else:
        return mayor(hijoder(arbol))
    
#eliminar en ABB
def eliminar(ele, a):
    if a == []:
        return []
    elif ele < raiz(a):
        return arbol (raiz(a), eliminar(ele, hijoizq(a)),hijoder(a))
    elif ele > raiz(a):
        return arbol (raiz(a),hijoizq(a), eliminar(ele, hijoder(a)))
    # nodo no tiene hijos
    elif hijoder(a) == [] and hijoizq(a) == []:
        return []
    # nodo no tiene hijo izquierdo
    elif hijoizq(a) == []:
        return hijoder(a)
    # nodo no tiene hijo derecho
    elif hijoder(a) == []:
        return hijoizq(a)
    else:
        return arbol(mayor(hijoizq(a)),
                     eliminar(mayor(hijoizq(a)),
                    hijoizq(a)),hijoder(a))



    
####################################################
#Hacer los siguientes ejercicios sobre árboles
####################################################

#convertir en lista ordenada, dado un ABB
#E: abb
#S: lista
def convertir_a_lista (arb):
    if arb == []:
        return []
    return  convertir_a_lista (hijoizq(arb)) + [raiz(arb)] + convertir_a_lista (hijoder(arb))

#retornar una lista de listas con lista raíz, lista menores y lista mayores
#[[10], [,2,5,6,7], [20,90]] en inOrden, es decir ordenados
def descomponer_arbol(arb):
    root = [raiz(arb)]
    menores = convertir_a_lista (hijoizq(arb))
    mayores = convertir_a_lista (hijoder(arb))
    return [root, menores, mayores]

#Lap 1
#buscar un elemento en un arbol binario (no necesariamente ordenado). Si
# se encuentra el elemento, se retorna True, False sino.
#E: elemento, arbol binario
#S: booleano
def buscar_ab(elemento, arb):
    if arb == []:
        return False
    elif elemento == raiz(arb):
        return True
    else:
        return buscar_ab(elemento, hijoizq(arb))  or  buscar_ab(elemento, hijoder(arb))
    
#Lap 1
# #buscar un elemento en un arbol binario ordenado (ABB). Si
# se encuentra el elemento, se retorna True, False sino.
#E: elemento, arbol bb
#S: booleano
def buscar_abb(elemento, arb):
    if arb == []:
        return False
    elif elemento == raiz(arb):
        return True
    elif elemento < raiz(arb):
        return buscar_abb(elemento, hijoizq(arb))
    else:
        return buscar_abb(elemento, hijoder(arb))

# retorne la profundidad de un árbol binario ** ver con el profe **
# retorne la altura de un árbol binario ** ver con el profe **

#Lap 2
# dado un elemento, retorne una lista con la ruta desde la raíz para llegar
# a ese elemento. Considere que es un ABB.
# 8,  [10, [5,2,8],[20,15,90]]  >>>  [10, 5 , 8]
# 20, [10, [5,2,8],[20,15,90]]  >>>  [10, 20]
def ruta (elemento, arb):
    if arb == []:
        return [ ]
    elif elemento == raiz(arb):
        return [raiz(arb)]
    elif elemento < raiz(arb):
        return [raiz(arb)] + ruta(elemento, hijoizq(arb))
    else:
        return [raiz(arb)] + ruta(elemento, hijoder(arb))

#Lap 2
#haga un algoritmo que retorne el nodo mayor de un AB (no ordenado).
def mayor_ab(arb):
    return mayor_ab_aux (arb, raiz(arb))

def mayor_ab_aux (arb, raiz_original):
    if arb == []:
        return raiz_original
    return max (raiz(arb), mayor_ab_aux (hijoizq(arb), raiz_original), mayor_ab_aux (hijoder(arb), raiz_original))

#Lap 2
#haga un algoritmo que retorne el nodo mayor de un ABB. Haga otro para el menor.
def menor (arbol):
    if hijoizq(arbol) == []:
        return raiz(arbol)
    else:
        return menor(hijoizq(arbol))

#Lap 2
#haga un algotirmo que dado un elemento, retorne la cantidad de veces que aparece
#ese elemento en el arbol binario (no necesariamente ABB).
# 8,  [10, [5,2,8],[20,15,90]]  > 1
# 2,  [10, [5,2,8],[2,15,2]]    > 3
# -6, [10, [5,2,8],[20,15,90]]  > 0
def apariciones(elemento, arb):
    if arb == []:
        return 0
    elif raiz(arb) == elemento:
        return 1 + apariciones(elemento, hijoizq(arb)) + apariciones(elemento, hijoder(arb))
    else:
        return apariciones(elemento, hijoizq(arb)) + apariciones(elemento, hijoder(arb))


def es_conjunto(arb):
    return es_conjunto_aux (arb, arb)
def es_conjunto_aux (arb, arb_original):
    if arb == []:
        return True
    elif apariciones(raiz(arb), arb_original) > 1:
        return False
    else:
        return es_conjunto_aux(hijoizq(arb), arb_original) and es_conjunto_aux(hijoder(arb), arb_original)

#Árbol Perfecto
#Determine si el árbol es perfecto (todos los niveles completamente llenos
#y todas las hojas en el mismo nivel).



#quiz


