# Iniciamos en 1 minutos


# Temas
# Función auxiliar
# Parámetros por omisión
# Recursividad de pila en algoritmos numéricos
# Recursividad de pila en listas
# 12 ejercicios de práctica con el profesor
# Tarea


#Haga una función que retorne la cantidad de divisores que tiene un número entero.
# divisores(10) retorna 4  #1,2,5,10

#caso base:    si num == divisor  >>> 1   #es parte del resultado   #si num < divisor   >>> 0
#              si num % divisor == 0
#                   return 1 + divisores (num, divisor + 1)
#               else:
#                        return divisores (num, divisor +1)

#E: un numero entero
#S: un número
def divisores (numero):
        numero = abs(numero)
        return divisores_aux (numero, 1)


#E: un numero entero, un divisor que debe empezar en 1
#S: un número
def divisores_aux(num, divisor):
        if num == divisor:
                return 1
        elif num % divisor == 0:
                return 1 + divisores_aux(num, divisor+1)
        else:
                return divisores_aux(num, divisor+1)
                
        
# parámetros por omisión
def divisores_v2 (num, divisor = 2):
        if num == divisor:
                return 1
        elif num % divisor == 0:
                return 1 + divisores_v2(num, divisor+1)
        else:
                return divisores_v2(num, divisor+1)
        
                

#algoritmos numéricos

def recorrido_numero (num):
        res = 0
        while num > 0:
                #lo que necesiten con la unidad
                num = num // 10
        return res


#recursividad
'''
365  // 10   +1
36   // 10   +1
3    // 10   +1
0
'''

#si num == 0   caso base
#sino  algo + funcion_rec (num//10)


def recorrido_recursivo(num):
        if num == 0:
                print(num, 'Caso base')
                return 0
        else:
                print(num, 'Caso recursivo')
                return recorrido_recursivo(num//10)


#dado un numero entero positivo o cero retorne la sumatoria
# de todos los digito de ese numero
#ejemplo: sumatoria (365)  >  14   #5+6+3
#E: numero
#S: numero

def sumatoria(num):
        if num == 0:
                return 0
        else:
                digito = num%10
                return digito + sumatoria(num//10)



#dado un numero entero, retorne la cantidad de digitos del numero
# haga una función recursiva
def cantidad_de_digitos(num):
        num = abs(num)
        return cantidad_de_digitos_aux(num)

def cantidad_de_digitos_aux(num):
        if num <= 9:
                return 1 #???
        else:
                return 1 + cantidad_de_digitos_aux(num//10)



'''
Implemente una función recursiva que cuente cuántos dígitos del número recibido son múltiplos de 3. Ejemplo: 
contar_multiplos_3(936) → 3   #(9, 3, 6)
'''

def contar_multiplos_3(num):
        if num == 0:
                return 0
        elif (num%10) % 3 == 0: #num%10 == 3 or num%10 == 6 or num%10 == 9
                return 1 + contar_multiplos_3(num//10)
        else:
                return contar_multiplos_3(num//10)

'''
Cree una función recursiva que calcule el producto de los dígitos de un número. Ejemplo: 
producto_digitos(234) → 2 * 3 * 4 = 24
'''
def producto_digitos(num):
        if num == 0:
                return 1
        else:
                return num%10 * producto_digitos(num//10)


'''
Cree una función recursiva que sume todos los números impares desde 1 hasta n.Ejemplo: suma_impares(5) → 1 + 3 + 5 = 9
'''
def sumatoria_impares(num):
        if num == 0:
                return 0
        elif num % 2 == 1:  #si es impar
                return num%10 + sumatoria_impares(num//10)
        else:
                return sumatoria_impares(num//10)
'''
Dado un número entero positivo, contar recursivamente cuántos dígitos son mayores que 5.Ejemplo: contar_mayores_5(2687) → 2 (6 y 8)
'''

def contar_mayores_que_5(num):
        if num == 0:
                return 0
        res = 0
        if (num%10) > 5: # solo si el digito es mayor que 5, pone res = 1
                res = 1

        return res + contar_mayores_que_5(num//10)


def contar_mayores_que_5(num):
        if num == 0:
                return 0
        if (num%10) > 5:
                return 1 + contar_mayores_que_5(num//10)
        else:
                return  contar_mayores_que_5(num//10)



#dado un número entero positivo retorne un número compuesto
#por sus digitos pares.
#E: numero
#S: numero
def solo_pares (num, exp = 0):
        if num == 0:
                return 0
        elif num%2 == 0: #es par
                return (num%10)*(10**exp) + solo_pares (num//10, exp + 1)
        else:
                return solo_pares (num//10, exp)



# recursivamente la sumatoria de los numeros de una lista


'''
f[1,2,3,4,5] =  1 + f[2,3,4,5]      lista[1:]
f[2,3,4,5] =    2 + f[3,4,5]
f[3,4,5] =      3 + f[4,5]
f[4,5] =        4 + f[5]
f[5] =          5 + f[]
[] paran es el caso base 0,[], 1 
'''


def recorrido_rec_lista(lista):
        if lista == []:
                print (lista, 'caso base')
                return 0
        else:
                print (lista[0], lista, 'llamada rec')
                return lista[0] + recorrido_rec_lista(lista[1:])


def suma_lista(lista):
        if lista == []:
                return 0
        else:
                return lista[0] + suma_lista(lista[1:])


#retorne una lista
#dada una lista de números, retorne solo los elemento pares
#E: lista
#S: lista

def solo_pares_lista(lista):
        if lista == []:
                return []
        elif lista[0] % 2 == 0: #si el primer elemento es par
                return [lista[0]] + solo_pares_lista(lista[1:])
        else:
                return solo_pares_lista(lista[1:])

# Pila - es rec simple
#retorne True or False

#dada una lista de numeros, retorne True si todos son positivos


#E: lista
#S: boolean
def son_todos_positivos(lista):
        if lista == []:
                return True
        elif lista[0] <= 0:
                return False
        else:
                return son_todos_positivos(lista[1:])
        

def son_todos_positivos(lista):
        if lista == []:
                return True
        elif lista[0] <= 0:
                return False
        else:
                return son_todos_positivos(lista[1:])



'''
Cree una función recursiva que reciba una lista y un elemento, y
retorne cuántas veces aparece ese elemento en la lista.
Ejemplo:contar([1,2,1,3,1], 1) → 3
'''
#E: lista, elemento
#S: numero
def contar(lista, elemento):
        if lista == []:
                return 0 #no debo afectar lo que acumulo, al final un cero para no afectar
        elif lista[0] == elemento:
                return 1 + contar(lista[1:], elemento)
        else:
                return  contar(lista[1:], elemento)

'''
Escriba una función recursiva que cuente cuántos elementos de una lista
son mayores a un valor dado.Ejemplo: mayores_a([3, 8, 1, 6], 4) → 2
'''
#E: lista, elemento
#S: numero
def mayores_a(lista, elemento):
        if lista == []: 
                return 0  #no afecto el acumulado en la pila, además en [] no hay amyores a elemento
        elif lista[0] > elemento:
                return 1 +  mayores_a(lista[1:], elemento)
        else:
                return  mayores_a(lista[1:], elemento)
'''
Implemente una función recursiva que retorne una nueva lista con cada
valor multiplicado por 2.Ejemplo: duplicar([1, 3, 5]) → [2, 6, 10]
'''
#E: lista, 
#S: lista
def duplicar(lista):
        if lista == []:
                return []   #no afecto el acumulado, como es lista concateno []
        else:
                return [lista[0] * 2] + duplicar(lista[1:])

'''
Cree una función recursiva que indique si ningún valor se repite en la lista.
Ejemplo: todos_distintos([1, 2, 3, 4]) → True

lista           original
[1,2,3,4]       [1,2,3,4]
'''
#E: lista, 
#S: boolean
def todos_distintos(lista):
        return todos_distintos_aux(lista, lista)

def todos_distintos_aux(lista, original):
        if lista == []:
                return True
        elif contar(original, lista[0]) > 1:
                return False
        else:
                return todos_distintos_aux(lista[1:], original)


def todos_distintos_v2(lista):
        if lista == []:
                return True
        elif contar(lista, lista[0]) > 1:
                return False
        else:
                return todos_distintos_v2(lista[1:])


        
'''
Cree una función recursiva que convierta un número entero a su
representación binaria como string.Ejemplo: a_binario(5) → '101'
'''
def a_binario (num, exp = 0):
        if num == 0:
                return 0
        return (num%2) * (10**exp) + a_binario (num//2, exp + 1)
        

#quién es el mayor entre dos numeros
def mayor_de (num1, num2):
        if num1 > num2:
                return num1
        return num2

'''
Implemente una función recursiva que encuentre el número mayor en una
lista de enteros (no usar max). Ejemplo:maximo([3, 9, 1, 5]) → 9
'''
#E: lista
#S: numero
def maximo (lista):
        if len(lista) == 1: #no puedo llegar a [] porque no hay elementos, caso base es len 1
                return lista[0]
        else:
                return mayor_de(lista[0], maximo(lista[1:]))





                              







