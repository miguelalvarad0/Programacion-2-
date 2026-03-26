
# Dado un numero entero no negativo retorne la cantidad de dígitos del número
# E: numero
# S: numero

def cantidad_digitos_pila (num):
        if num == 0:
                return 0
        return 1 + cantidad_digitos_pila(num//10)

'''
cantidad_digitos_pila (365)
        1 + cantidad_digitos_pila (36)
            1 + cantidad_digitos_pila (3)
                1 + cantidad_digitos_pila (0)
                    0
'''
#1. deben tener un argumento resultado
#2. la operación la ponen en el argumento resultado
#3. no retornen un valor en los casos base, retornen el resultado

def cantidad_digitos_cola (num, resultado = 0):
        #print ('resultado lleva: ', resultado)
        if num < 10:
                return resultado + 1
        resultado += 1
        return cantidad_digitos_cola(num//10, resultado)



#E: lista
#S: lista
 
def sin_repetidos(lista, resultado = []):
        if lista == []:
                return resultado
        elif lista[0] in resultado:
                return sin_repetidos(lista[1:], resultado)
        else:
                return sin_repetidos(lista[1:], resultado + [lista[0]])




def elimina_pares (num, exp = 0):
        if num == 0:
                return 0
        elif num % 2 == 0: #si es par, no se suma nada a la pila
                return elimina_pares (num//10, exp)
        else:
                return (num%10)*(10**exp) + elimina_pares (num//10, exp+1)




#1. deben tener un argumento resultado
#2. la operación la ponen en el argumento resultado
#3. no retornen un valor en los casos base, retornen el resultado

def elimina_pares_c (num, exp = 0, res = 0):
        print(exp, '     res:', res)
        if num == 0:
                return res
        elif num % 2 == 0: #si es par, no se suma para que se pierda
                return elimina_pares_c (num//10, exp, res)
        else:
                return elimina_pares_c (num//10, exp+1, res + (num%10)*(10**exp))





#contar multiplos de 3
#E: numero
#S: numero


def contar_multiplos_3 (num):
        if num == 0:
                return 1 # se supone que el cero es divisible por 3
        else:
                return contar_multiplos_3_aux(num,0) # ojo: acá desde la auxiliar le podemos pasar el valor del resultado, se usa cuando el valor debe ser un calculo que no puede ser valor default

def contar_multiplos_3_aux(num, contador):
        if num == 0:
                return contador
        elif (num%10) % 3 == 0:
                return contar_multiplos_3_aux(num//10, contador +1)
        else:
                return contar_multiplos_3_aux(num//10, contador)





#producto digitos
#E: numero
#S: numero
def producto_digitos (num, producto = 1):
        if num < 10:
                return producto * num
        return producto_digitos (num // 10, producto * (num%10))


'''
Cree una función recursiva que reciba una lista y un elemento,
y retorne cuántas veces aparece ese elemento en la lista.
Ejemplo:contar([1,2,1,3,1], 1) → 3
'''
#E: lista, elemento
#S: numero

#nota: este lo solucioné en el if preparando el argumento, al final
# llamo la recursividad con el argumento cambiado o no, según entró al if
def contar (lista, elemento, contador = 0):
        if lista == []:
                return contador
        elif lista[0] == elemento:
                contador += 1
        return contar (lista[1:], elemento, contador)

'''
Implemente una función recursiva que determine si una lista
de enteros está ordenada de forma ascendente.
Ejemplo:esta_ordenada([1, 3, 5, 7]) → True,
esta_ordenada([1, 5, 3]) → False
'''
#E: lista
#S:boolean
#nota: tengo un argumento en True, que cambiaré a False sii
#encuentro desorden, sino, al final nunca cambió y será True

def esta_ordenada (lista, respuesta = True):
        if len(lista) == 1 or lista == []:
                return respuesta
        elif lista[0] > lista[1]: #si primer elemento es mayor que siguiente, está desordenada y cambio a False
                return esta_ordenada (lista[1:], False)
        else:
                return esta_ordenada (lista[1:], respuesta) #si está ordenada no cambio respuesta, para que mantenga su False si antes entró el if de arriba, o el True si no ha cambiado


#E: numero
#S: numero invertido
def invertir_numero (num):
        exp = cantidad_digitos_cola(num) - 1 # necesito un exponente de cantidad de digitos menos uno para que reconstruya de izquierda a derecha
        return invertir_aux (num, exp, 0)

def invertir_aux (num, exp, resultado):
        print(num, exp, resultado)
        if num == 0:
                return resultado
        nuevo_digito = (num % 10) * (10**exp) #calculo el nuevo dígito
        exp -= 1  # al exp se le resta, porque inicié en cant-1
        return invertir_aux (num//10, exp, resultado + nuevo_digito)


#E: lista de numeros
#S: numero
#lista con al menos 1 elemento

def maximo (lista):
        return maximo_aux (lista[1:], lista[0])
        #nota: le quito 1 elemento a la lista porque lo envío como max_actual de segundo argumento

def maximo_aux (lista, max_actual):
        if lista == []:
                return max_actual
        elif lista[0] > max_actual:  #si lista[0] es mejor o mayor, llamo a la recursividad con lista[0] como el argumento max_actual porque fue el que encontré mejor hasta el momento
                return maximo_aux (lista[1:], lista[0])
        else:
                return maximo_aux (lista[1:], max_actual) # no cambio max_actual porque lista[0] no es mayor



'''
Cree una función recursiva que indique si ningún valor se repite en la lista.
Ejemplo: todos_distintos([1, 2, 3, 4]) → True
'''

#respuesta inicia en True, si encuentro repetido, cambia a False y nunca más volverá a True
def todos_distintos(lista, respuesta = True):
        if lista == []:
                return respuesta
        elif lista[0] in lista[1:]: #si el primer elemento está en el resto de la lista, quiere decir que repite
                return todos_distintos(lista[1:], False)
        return todos_distintos(lista[1:], respuesta)



'''
suma de impares de 1 hasta n
'''
def suma_impares (n, contador = 0):
        if n == 0:
                return contador
        return suma_impares (n-1, contador + n)


#contar mayores que 5
def contar_mayores_5 (num, contador = 0):
        if num == 0:
                return contador
        elif num%10 > 5:
                contador += 1
        return contar_mayores_5 (num//10, contador) #contador aumento si entró al elif


# a_binario
#debe usar exponente para reconstruir el numero
def a_binario (num, exp = 0, res = 0):
        if num == 0:
                return res
        nuevo_digito = (num%2) * (10**exp)
        return a_binario(num//2, exp + 1, res + nuevo_digito)


def duplicar (lista, res = []):
        if lista == []:
                return res
        return duplicar(lista[1:], res + [lista[0]*2])


def mayores_a (lista, elemento, res = []):
        if lista == []:
                return res
        elif lista[0] > elemento:
                return mayores_a (lista[1:], elemento, res + [lista[0]])
        else:
                return mayores_a (lista[1:], elemento, res)







