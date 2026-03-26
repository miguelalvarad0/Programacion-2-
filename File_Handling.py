def read_grades():
    datos = []

    with open("registros.txt", "r") as archivo:
        for linea in archivo:
            nombre, materia, nota = linea.strip().split(",")
            datos.append([nombre, materia, int(nota)])

    return datos
read_grades()
def print_average():
    datos = read_grades()

    promedios = {}
    conteo = {}

    for nombre, materia, nota in datos:
        if nombre not in promedios:
            promedios[nombre] = 0
            conteo[nombre] = 0

        promedios[nombre] += nota
        conteo[nombre] += 1

    for nombre in promedios:
        promedio = promedios[nombre] / conteo[nombre]
        print(f"{nombre}: {promedio}")
print_average()

def write_average():
    datos = read_grades()

    promedios = {}
    conteo = {}

    for nombre, materia, nota in datos:
        if nombre not in promedios:
            promedios[nombre] = 0
            conteo[nombre] = 0

        promedios[nombre] += nota
        conteo[nombre] += 1

    with open("promedios.txt", "w") as archivo:
        for nombre in promedios:
            promedio = promedios[nombre] / conteo[nombre]
            archivo.write(f"{nombre}: {promedio}\n")
write_average()

def process_log():
    actividades = {}

    with open("bitacora.log") as archivo:
        for linea in archivo:
            partes = linea.strip().split()
            usuario = partes[3]  # nombre después de "Usuario"

            actividades[usuario] = actividades.get(usuario, 0) + 1

    # usuario más activo
    mas_activo = max(actividades, key=actividades.get)
    print(mas_activo)

    # escribir archivo de salida
    with open("user_activity.txt", "w") as salida:
        for usuario, total in actividades.items():
            salida.write(f"Usuario {usuario} tiene {total} actividades\n")
process_log()

def read_map():
    matriz = []

    with open("mapa.txt") as archivo:
        for linea in archivo:
            fila = list(linea.strip())
            matriz.append(fila)

    # recorrer la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "X":
                print(f"({i},{j})", end=" ")
read_map()
