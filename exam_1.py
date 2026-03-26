# 1. digitos_comunes_mayores(num1, num2, limite)
# Escriba un programa en Python llamado digitos_comunes_mayores(num1, num2, limite)
# que recibe 2 números enteros y un límite (0–9), y retorna otro número conformado por los
# dígitos comunes a ambos números que además sean mayores o iguales al límite. Si
# no existen, retorne -1.
# Restricción:
# No puede invertir los números, convertirlos a string o listas.
# Ejemplos:
# • digitos_comunes_mayores(241, 42542, 3) retorna 4
# • digitos_comunes_mayores(30241, 425420, 2) retorna 24 o 42
# • digitos_comunes_mayores(123, 987, 5) retorna -1
# 2. cut(lista)
# Escriba una función recursiva llamada cut(lista) que reciba una lista y produce una lista de
# listas, cortando cada sublista cuando aparecen números ceros.
# >>> cut([1,23,0,29,2,0,1,0,34])
# [[1, 23], [29, 2], [1], [34]]
# >>> cut([1,2,0,0,0])
# [[1, 2]]
# >>> cut([1,2,3,4])
# [[1, 2, 3, 4]]
# 3. elimine(num, dig) 
# Escriba un programa en Python llamado elimine(num, dig) que recibe un número entero
# posi8vo o cero y retorna un número sin los dígitos iguales al dígito dado, excepto el dígito
# más significa8vo, es decir, recorriendo el número de izquierda a derecha y eliminando los
# iguales en el número dado a excepción del que está más a la izquierda. No puede inver8r
# el número ni conver8rlo a lista, string u otro iterable.
# Recuerde que para recorrer un número de izquierda a derecha necesita un exponente de
# can8dad de dígitos menos uno e ir aplicando la formula:
# digitoDerecho = ( num//(10**exp) ) % 10, por ejemplo:
# Para 8457 requiere exponente = 3 (can8dad dígitos - 1)
# ( 8457// (10**3) ) % 10 => 8
# ( 8457// (10**2) ) % 10 => 4
# ( 8457// (10**1) ) % 10 => 5
# ( 8457// (10**0) ) % 10 => 7
# Exp llega a -1 y podrá terminar.
# Ejemplos:
# > elimine(135232, 2) retorna 13523
# > elimine(555, 5) retorna 5
# > elimine(1002010402, 0) retorna 102142 



def contiene_digito(numero, digito):
    if numero == 0:
        return False
    if numero%10 == digito:
        return True
    return contiene_digito(numero // 10, digito)

def digitos_comunes_mayores(num1,num2,limite):
    def digitos_comunes_mayores_2(n1):
        if n1 == 0:
            return 0
        digito = n1 % 10
        restante = digitos_comunes_mayores_2(n1//10)

        if digito > limite and contiene_digito(num2, digito):
            return restante * 10 + digito
        else:
            return restante

    respuesta = digitos_comunes_mayores_2(num1)
    return respuesta if respuesta != 0 else -1

print(digitos_comunes_mayores(241, 42542, 3))

def cut(lista):
#caso de parada siempre es cuando la lista ya esta vacia
    if lista == []:
        return [[]]

    resto = cut(lista[1:])

    if lista[0] == 0:
        return [[]] + resto
    else:
        resto[0] = [lista[0]] + resto[0]
        return resto

print(cut([1,23,0,29,2,0,1,0,34]))

def elimine(num, dig):
    def contar_digitos(n):
        if n < 10:
            return 1
        return 1 + contar_digitos(n // 10)

    def auxiliar(n, exp, encontrado):
        if exp < 0:
            return 0

        d = (n // (10 ** exp)) % 10
        resto = auxiliar(n, exp - 1, encontrado or d == dig)

        if d == dig and encontrado:
            return resto  # se elimina
        else:
            return d * (10 ** contar_digitos(resto)) + resto

    return auxiliar(num, contar_digitos(num) - 1, False)

print(elimine(555, 5))