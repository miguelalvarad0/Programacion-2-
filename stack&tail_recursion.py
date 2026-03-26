def reemplazar_pila(lista, x, y, indice=0):

    if indice == len(lista):
        return lista


    reemplazar_pila(lista, x, y, indice + 1)


    if lista[indice] == x:
        lista[indice] = y

    return lista
lista = [1, 2, 3, 2, 4, 2]
resultado = reemplazar_pila(lista, 2, 9)
print(resultado)

def reemplazar_cola(lista, x, y, indice=0):

    if indice == len(lista):
        return lista


    if lista[indice] == x:
        lista[indice] = y


    return reemplazar_cola(lista, x, y, indice + 1)

lista2 = [1, 2, 3, 2, 4, 2]
resultado = reemplazar_cola(lista2, 2, 9)
print(resultado)

def contar_mayor_recursivo(lista, maximo=None, indice=0):
    if maximo is None:
        maximo = max(lista)

    if indice == len(lista):
        return 0

    if lista[indice] == maximo:
        return 1 + contar_mayor_recursivo(lista, maximo, indice + 1)
    else:
        return contar_mayor_recursivo(lista, maximo, indice + 1)

lista3 = [4, 2, 7, 7, 3, 7, 1]
resultado = contar_mayor_recursivo(lista3)
print(resultado)

def contar_mayor_cola(lista, indice=0, maximo=None, contador=0):
    if indice == 0:
        maximo = max(lista)

    if indice == len(lista):
        return contador

    if lista[indice] == maximo:
        contador += 1

    return contar_mayor_cola(lista, indice + 1, maximo, contador)

lista4 = [4, 2, 7, 7, 3, 7, 1]
resultado = contar_mayor_cola(lista4)
print(resultado)

def suma_digitos_pares_pila(n, posicion=0):
    if n == 0:
        return 0

    digito = n % 10

    if posicion % 2 == 0:
        return digito + suma_digitos_pares_pila(n // 10, posicion + 1)
    else:
        return suma_digitos_pares_pila(n // 10, posicion + 1)

numero = 482736
resultado = suma_digitos_pares_pila(numero)
print(resultado)

def suma_digitos_pares_cola(n, posicion=0, suma=0):
    if n == 0:
        return suma

    digito = n % 10

    if posicion % 2 == 0:
        suma += digito

    return suma_digitos_pares_cola(n // 10, posicion + 1, suma)

numero2 = 482736
resultado = suma_digitos_pares_cola(numero2)
print(resultado)

def eliminar_primer_negativo_pila(lista):
    if not lista:
        return []

    if lista[0] < 0:
        return lista[1:]

    resto = eliminar_primer_negativo_pila(lista[1:])

    return [lista[0]] + resto

lista = [4, 6, -3, 2, -8, 5]
print(eliminar_primer_negativo_pila(lista))

def eliminar_primer_negativo_cola(lista, indice=0, eliminado=False):
    if indice == len(lista):
        return lista

    if not eliminado and lista[indice] < 0:
        lista.pop(indice)
        eliminado = True
        return eliminar_primer_negativo_cola(lista, indice, eliminado)

    return eliminar_primer_negativo_cola(lista, indice + 1, eliminado)

lista6 = [4, 6, -3, 2, -8, 5]
resultado = eliminar_primer_negativo_cola(lista6)
print(resultado)

def contar_mayores_pila(numero, indice=0):
    numero_str = str(numero)

    if indice == len(numero_str) - 1:
        return 0

    actual = int(numero_str[indice])
    siguiente = int(numero_str[indice + 1])

    if actual > siguiente:
        return 1 + contar_mayores_pila(numero, indice + 1)
    else:
        return contar_mayores_pila(numero, indice + 1)

numero5 = 752431
resultado = contar_mayores_pila(numero5)
print(resultado)

def contar_mayores_cola(numero, indice=0, contador=0):
    numero_str = str(numero)

    if indice == len(numero_str) - 1:
        return contador

    actual = int(numero_str[indice])
    siguiente = int(numero_str[indice + 1])

    if actual > siguiente:
        contador += 1

    return contar_mayores_cola(numero, indice + 1, contador)

numero6 = 752431
resultado = contar_mayores_cola(numero6)
print(resultado)