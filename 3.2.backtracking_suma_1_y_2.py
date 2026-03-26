def sumar_con_1_y_2(n, combinacion=[]):
    if sum(combinacion) == n:
        print("SOLUCION >>> ",combinacion)
        return
    if sum(combinacion) > n:
        return  # nos pasamos, hay que retroceder
    sumar_con_1_y_2(n, combinacion + [1])
    sumar_con_1_y_2(n, combinacion + [2])

# Ejemplo:
sumar_con_1_y_2(4)


s(4, [])









