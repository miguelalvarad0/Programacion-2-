

#crear un mapa de nxm caracteres
# E: ruta_nombre del archivo, filas, columnas, caracter
# R: none (crea el archivo)

def create_raw_map(filename, rows, columns, char):
        with open(filename, 'w') as file: #abrir el archivo
                line = char * columns   #crea el string con los carecters de una línea
                for _ in range(rows):          #filas veces
                        file.write(line + '\n') #escribe la línea

#lee el archivo linea a linea y retorna un matriz con cada línea
def read_map (filename):
        matrix = []
        with open(filename, 'r') as file: #abrir el archivo
                for line in file:       #es file es iterable, se recorre por linea
                        matrix.append(line[:-1]) #se hace push de cada linea en la matrix
        return matrix



#cambia un caracter en el punto x,y del mapa
#E: archivo, fila,columna, caracter nuevo
#S: none

def change_character(filename, row, col, new_char):
        with open(filename, 'r+') as file:
                row_lenght = len(file.readline()) #averiguar largo de las filas
                file.seek(0)  #devolver cursor al inicio
                offset = row * row_lenght + col
                file.seek(offset) #salto al caracter que se quiere cambiar
                file.write(new_char) #escribe el char nuevo



#dibuja caminos horizontales y verticales dada lista de puntos (tuplas (x,y))
#E: archivo, caracter, lista_coordenadas [(4,6),(10,6),(10 ,19)]
#S: none
def draw_path (filename, new_char, coord_list):
        with open(filename, 'r+') as file:
                row_lenght = len(file.readline()) #averiguar largo de las filas
                file.seek(0)  #devolver cursor al inicio

                for i in range(len(coord_list) - 1):
                        row1, col1 = coord_list[i]
                        row2, col2 = coord_list[i + 1]

                        if row1 == row2:  # horizontal 
                                for c in range(min(col1,col2), max(col1,col2)+1):
                                        offset = row1 * row_lenght + c
                                        file.seek(offset)
                                        file.write(new_char)
                        elif col1 == col2: #vertical
                                for r in range(min(row1,row2), max(row1,row2)+1):
                                        offset = r * row_lenght + col1
                                        file.seek(offset)
                                        file.write(new_char)                                
                        else:
                                print('Error de coordenadas')

                        
