def contar_digito(n, d):
    def contar_aux(n, d, contador):

        if n == 0:
            return contador


        if n % 10 == d:
            contador += 1


        return contar_aux(n // 10, d, contador)


    if n == 0:
        return 1 if d == 0 else 0

    return contar_aux(abs(n), d, 0)
def es_primo(n):
    def es_primo_aux(n, divisor):

        if divisor * divisor > n:
            return True


        if n % divisor == 0:
            return False


        return es_primo_aux(n, divisor + 1)


    if n <= 1:
        return False

    return es_primo_aux(n, 2)

def contar_ceros(n):
    def contar_aux(n, contador):

        if n == 0:
            return contador

        if n % 10 == 0:
            contador += 1

        return contar_aux(n // 10, contador)

    if n == 0:
        return 1

    return contar_aux(n, 0)

def todos_digitos_pares(n):
    def aux(n):
        if n < 10:
            return n % 2 == 0

        if (n % 10) % 2 != 0:
            return False

        return aux(n // 10)

    return aux(n)

def suma_digitos_alternados(n):
    def contar_digitos(n):
        if n < 10:
            return 1
        return 1 + contar_digitos(n // 10)

    def aux(n, potencia, signo, acumulador):
        if potencia == 0:
            return acumulador

        digito = n // potencia

        acumulador += signo * digito

        return aux(n % potencia, potencia // 10, -signo, acumulador)

    total_digitos = contar_digitos(n)
    potencia = 10 ** (total_digitos - 1)

    return aux(n, potencia, 1, 0)

def eliminar_digitos_pares(n):
    def aux(n, acumulador, potencia):
        if n == 0:
            return acumulador

        digito = n % 10

        if digito % 2 != 0:
            acumulador += digito * potencia
            potencia *= 10

        return aux(n // 10, acumulador, potencia)

    if n == 0:
        return 0

    return aux(n, 0, 1)

def eliminar_duplicados(lista):
    def aux(lista, i, resultado):
        if i == len(lista):
            return resultado

        if lista[i] not in resultado:
            resultado.append(lista[i])

        return aux(lista, i + 1, resultado)

    return aux(lista, 0, [])

def suma_posiciones_pares(lista):
    def aux(lista, i, acumulador):
        if i == len(lista):
            return acumulador

        if i % 2 == 0:
            acumulador += lista[i]

        return aux(lista, i + 1, acumulador)

    return aux(lista, 0, 0)

def suma_entre_posiciones(lista, i, j):
    def aux(lista, indice, i, j, acumulador):
        if indice > j:
            return acumulador

        if i <= indice <= j:
            acumulador += lista[indice]

        return aux(lista, indice + 1, i, j, acumulador)

    return aux(lista, 0, i, j, 0)

def suma_mayores_que_promedio(lista):
    if not lista:
        return 0

    promedio = sum(lista) / len(lista)

    def aux(lista, i, acumulador):
        if i == len(lista):
            return acumulador

        if lista[i] > promedio:
            acumulador += lista[i]

        return aux(lista, i + 1, acumulador)

    return aux(lista, 0, 0)

print(contar_digito(87568748, 8))
print(es_primo(5))
print(contar_ceros(102030))
print(todos_digitos_pares(2586))
print(suma_digitos_alternados(1234))
print(eliminar_digitos_pares(123456))
print(eliminar_duplicados([1, 2, 3, 2, 1, 4]))
print(suma_posiciones_pares([10, 20, 30, 40, 50]))
print(suma_entre_posiciones([10, 20, 30, 40, 50], 1, 3))
print(suma_mayores_que_promedio([1, 2, 3, 4, 5]))