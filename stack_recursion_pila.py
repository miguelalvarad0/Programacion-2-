def contar_digito(n, d):
    if n == 0:
        return 0
    
    ultimo = n % 10
    
    if ultimo == d:
        return 1 + contar_digito(n // 10, d)
    else:
        return contar_digito(n // 10, d)


def es_primo(n):
    if n <= 1:
        return False
    return verificar(n, 2)
def verificar(n, d):
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return verificar(n, d + 1)


def contar_ceros(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + contar_ceros(n // 10)
    else:
        return contar_ceros(n // 10)


def todos_digitos_pares(n):
    if n < 10:
        return n % 2 == 0
    if (n % 10) % 2 != 0:
        return False
    return todos_digitos_pares(n // 10)


def suma_digitos_alternados(n):
    def aux(n):
        if n < 10:
            return n
        resultado = aux(n // 10)
        if (len(str(n)) % 2) == 0:
            return resultado - (n % 10)
        else:
            return resultado + (n % 10)
    return aux(n)


def eliminar_digitos_pares(n):
    if n == 0:
        return 0
    resto = eliminar_digitos_pares(n // 10)
    digito = n % 10
    if digito % 2 != 0:
        return resto * 10 + digito
    return resto


def sin_duplicados(lista):
    if not lista:
        return []
    resto = sin_duplicados(lista[1:])
    if lista[0] in lista[1:]:
        return resto
    return [lista[0]] + resto


def suma_posiciones_pares(lista):
    def aux(lista, i):
        if i == len(lista):
            return 0
        suma_restante = aux(lista, i + 1)
        if i % 2 == 0:
            return lista[i] + suma_restante
        return suma_restante
    return aux(lista, 0)


def suma_entre_posiciones(lista, i, j):
    def aux(lista, indice, i, j):
        if indice == len(lista):
            return 0
        suma_restante = aux(lista, indice + 1, i, j)
        if i <= indice <= j:
            return lista[indice] + suma_restante
        return suma_restante
    return aux(lista, 0, i, j)


def suma_mayores_que_promedio(lista):
    if not lista:
        return 0
    promedio = sum(lista) / len(lista)

    def aux(lista, i):
        if i == len(lista):
            return 0
        suma_restante = aux(lista, i + 1)
        if lista[i] > promedio:
            return lista[i] + suma_restante
        return suma_restante

    return aux(lista, 0)


print(contar_digito(455454, 5)) 
print(es_primo(2)) 
print(contar_ceros(1050300))
print(todos_digitos_pares(2486)) 
print(suma_digitos_alternados(1234))
print(eliminar_digitos_pares(123456))
print(sin_duplicados([1, 2, 3, 2, 1, 4]))
print(suma_posiciones_pares([10, 20, 30, 40, 50]))
print(suma_entre_posiciones([10, 20, 30, 40, 50], 1, 3))
print(suma_mayores_que_promedio([1, 2, 3, 4, 5]))