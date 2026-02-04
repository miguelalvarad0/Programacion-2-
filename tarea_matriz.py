matriz1 = [[1,  2,  3,  4]
,
[11, 12, 13, 14]
,
[21, 22, 23, 24]
,
[31, 32, 33, 34]]
 
matriz2 = [[1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
,
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
,
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
,
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
,
[41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
,
[51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
,
[61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
,
[71, 72, 73, 74, 75, 76, 77, 78, 79, 80]]

def print_matrix(matriz):
        for fila in matriz:
                for elemento in fila:
                        print (elemento)

def recorrer(matriz):
        for i in range(len(matriz)):  #0....7  x8
                print('i:',i)
                for j in range(len(matriz[i])):  #0 .. 9  x10
                        print('i:',i, '    j:',j, '     ', matriz[i][j] )
                        
def imprimir(matriz):
        columnas = len(matriz[0]) #largo de la primera fila, me da las columnas
        print ('Cols:', end="\t")
        for i in range(columnas):
                print (i, end="\t")
        print()
                

        
        for i in range(len(matriz)):
                print('fila', i, end=':\t')  #aquí inicia el for que recorre la fila, por tanto se imprime el i
                for j in range(len(matriz[i])):
                        print(matriz[i][j], end='\t')
                print() #enter al final de cada fila, al terminar la fila se imprime enter

def sumatoria (matriz):
        filas = len(matriz)
        cols =  len(matriz[0])

        resultado = 0

        for i in range(filas):
                for j in range(cols):
                        #aquí es donde puedo usar cada uno de los elementos
                        resultado += matriz[i][j]
        return resultado
                        
def cantidad_pares (matriz):
        filas = len(matriz)
        cols =  len(matriz[0])
        resultado = 0

        for i in range(filas):
                for j in range(cols):
                        if matriz[i][j] % 2 == 0:
                                resultado += 1
                        
        print ('pares:',resultado)

def cantidad_impares (matriz):
        filas = len(matriz)
        cols =  len(matriz[0])
        resultado = 0

        for i in range(filas):
                for j in range(cols):
                        if matriz[i][j] % 2 != 0:
                                resultado += 1
                        
        print ('impares:',resultado)

def lista_pares (matriz):
        filas = len(matriz)
        cols =  len(matriz[0])
        resultado = []

        for i in range(filas):
                for j in range(cols):
                        elemento = matriz[i][j]
                        if elemento % 2 == 0:
                              resultado.append(elemento)  
                        
        return resultado

def todos_pares (matriz):
        filas = len(matriz)
        cols =  len(matriz[0])

        for i in range(filas):
                for j in range(cols):
                        if matriz[i][j] % 2 != 0:
                                return False
                        
        return True

def promedio_filas(matriz):
        for i in range(len(matriz)):  #0....7  x8
                suma = 0
                for j in range(len(matriz[i])):  #0 .. 9  x10
                        suma = suma + matriz[i][j]
                        prom = suma / len(matriz[i])
                print('promedio fila',i,':',prom)

def suma_columnas(matriz):
        
        filas = len(matriz)
        columnas = len(matriz[0])

        for j in range(columnas):
            suma = 0
            for i in range(filas):
                suma = suma + matriz[i][j]
            print('sumatoria columna',j,':',suma)                
               
def mayor_fila(matriz):
        lista = []
        for i in range(len(matriz)):  #0....7  x8
                suma = 0
                for j in range(len(matriz[i])):  #0 .. 9  x10
                        suma = suma + matriz[i][j]
                lista.append(suma)
        print('fila con mayor suma:',1+lista.index(max(lista)))

def posicion_mayor(matriz):
        valor = 0
        x = 0 
        y = 0
        for i in range(len(matriz)):  #0....7  x8               
                for j in range(len(matriz[i])):  #0 .. 9  x10
                        if matriz[i][j] > valor:
                                x = i
                                y = j
                                valor = matriz[i][j]
        print ('valor mayor:',valor, ', posicion:(',x,',',y,')')

def posicion_menor(matriz):
        valor = matriz[0][0]
        x = 0 
        y = 0
        for i in range(len(matriz)):  #0....7  x8               
                for j in range(len(matriz[i])):  #0 .. 9  x10
                        if matriz[i][j] < valor:
                                x = i
                                y = j
                                valor = matriz[i][j]
        print ('valor menor:',valor, ', posicion:(',x,',',y,')')

def diagonal(matriz):
        suma = 0
        if len(matriz) != len(matriz[0]):
                print('la matriz no es cuadrada')
        else:
            print('diagonal:', end="\t")
            for i in range(len(matriz)):  
                suma += matriz[i][i]
                print(' + ',matriz[i][i], end="\t")
            print('suma:',suma)
                
def positivos_filas(matriz):
        for i in range(len(matriz)):  #0....7  x8
                suma = 0
                for j in range(len(matriz[i])):  #0 .. 9  x10
                    if matriz[i][j] > 0: 
                        suma += 1
                print('positivos fila',i,':',suma,'/', end="\t")
        print()
def imprimir_inverso(matriz):
        filas = len(matriz)
        indice = filas - 1
        columnas = len(matriz[0]) 

        print('Intercambio de filas')

        print ('Cols:', end="\t")
        for i in range(columnas):
                print (i, end="\t")
        print()
                
        print('fila 0', end=':\t') 
        for j in range(len(matriz[i])):
            print(matriz[indice][j], end='\t')
        print()

        for i in range(1,len(matriz)-1):
                print('fila', i, end=':\t') 
                for j in range(len(matriz[i])):
                        print(matriz[i][j], end='\t')
                print() #enter al final de cada fila, al terminar la fila se imprime enter

        print('fila',filas-1, end=':\t') 
        for j in range(len(matriz[i])):
            print(matriz[0][j], end='\t')

imprimir(matriz1)
promedio_filas(matriz1)
suma_columnas(matriz1)
mayor_fila(matriz1)
cantidad_pares (matriz1)
cantidad_impares (matriz1)
posicion_mayor(matriz1)
posicion_menor(matriz1)
diagonal(matriz1)
positivos_filas(matriz1)
imprimir_inverso(matriz1)