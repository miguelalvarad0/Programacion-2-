




#1 REVISAR ALGUNA DUDA DE LA TAREA
#2 RECURSIVIDAD DE COLA

'''
Cree una función recursiva que reciba una lista y devuelva una nueva lista
sin duplicados, manteniendo el primero que aparece.
Ejemplo: sin_repetidos([1, 2, 1, 3, 2]) → [1, 2, 3]



sin_repetidos([1, 2, 1, 3, 2], CONTADOS = [])

[1] + sin_repetidos([2, 1, 3, 2], CONTADOS = [1])
   [2] + sin_repetidos([ 1, 3, 2], CONTADOS = [1,2])
           sin_repetidos([ 3, 2], CONTADOS = [1,2])
              [3] + sin_repetidos([ 2], CONTADOS = [1,2, 3])
                      sin_repetidos([],CONTADOS = [1,2, 3])
                      []
'''


#E: lista
#S: lista
def sin_repetidos(lista, contados = []):
        print(contados)
        if lista == []:
                return [ ]
        elif lista[0] in contados:
                return sin_repetidos(lista[1:], contados + [lista[0]])
        else:
                return [lista[0]] + sin_repetidos(lista[1:], contados + [lista[0]])
                
'''
2. Verificar si un número es primo
Cree una función recursiva que determine si un número es primo.
Ejemplo: es_primo(7) → True, es_primo(9) → False
'''
'''
es_primo(7, div = 2) ?
es_primo(7, div = 3) ?
es_primo(7, div = 7) ?
'''
#E: numero natural
#S: True or False
def es_primo(num):
        if num == 1:
                return False
        else:
                return es_primo_aux(num, 2)

def es_primo_aux (num, divisor):
        if divisor > (num//2):
                return True
        elif num % divisor == 0: #le encontré un divisor que no es 1 ni él mismo
                return False
        else:
                return es_primo_aux (num, divisor+1)
        

#contar divisores de un numero natural
#E: numero natural
#S: numero
# divisores_de (6) > 4   1,2,3,6
# divisores_de (7) > 2   1,7

def divisores_de(num, divisor = 1):
        if divisor > num:
                return 0
        elif num % divisor == 0:
                return 1 + divisores_de(num, divisor + 1)
        else:
                return divisores_de(num, divisor + 1)
        

def es_primo_v2 (num):
        return divisores_de(num) == 2



#contador de divisores mejorado
def divisores_de_v3(num, divisor = 1):
        if divisor > (num//2):
                return 1
        elif num % divisor == 0:
                return 1 + divisores_de_v3(num, divisor + 1)
        else:
                return divisores_de_v3(num, divisor + 1)
        

def es_primo_v3 (num):
        return divisores_de_v3(num) == 2




'''
6. Eliminar pares Haga una función que elimine los
dígitos pares de un número entero positivo o cero.
Considere el cero como par.
Ejemplo: elimina_pares (1234) retorna 13
elimina_pares (2034) retorna 3
'''

'''
5             1           2    3        4
10**2         10**1       0    x10**0   0

500 + 10 + 3   513

513
'''

def elimina_pares (num, exp = 0):
        if num == 0:
                return 0
        elif num % 2 == 0: #si es par, no se suma nada a la pila
                return elimina_pares (num//10, exp)
        else:
                return (num%10)*(10**exp) + elimina_pares (num//10, exp+1)









