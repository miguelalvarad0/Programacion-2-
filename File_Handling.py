#----------------------------------------------------
#variables globales: variables disponibles para todo el programa
estudiantes = []

FILENAME = 'estudiantes.txt'

#NOTA: un estudiantes será una lista de ID, nombre, lista de notas, privincia 
#Ejemplo: [1, 'Diego Mora', [100,99,98,100,90], 'Cartago']

#----------------------------------------------------
# funciones de manejo de archivos
#crea un archivo
#E: path del archivo
def crear_archivo(file_path):
        archivo = open(file_path, 'w') # w crea o trunca el archivo
        archivo.close()

#guarda un string en un archivo. Le cae encima al contenido del archivo
#E: path del archivo, contenido
def guardar_archivo(file_path, content):
        archivo = open(file_path, 'w') # w crea o trunca el archivo
        archivo.write(content)
        archivo.close()

#lee la información de un archivo
#E: path
#S: string con el contenido del archivo
def leer_archivo(path):
        archivo = open(path, 'r')
        contenido = archivo.read()
        archivo.close()
        return contenido


#-------------------------------------
#carga el archivo de estudiantes en la lista  DISCO >>> MEMORIA
def cargar_estudiantes():
        global estudiantes
        strLista = leer_archivo(FILENAME)
        if strLista != '':
                estudiantes = eval(strLista)

#CRUD de estudiantes
#Create: insertar un estudiante
#Read: lee los estudiantes
#Update: actualiza un estudiante
#Delete: elimina un estudiante


#buscar_por_id
#dado un id, retorn la lista del estudiante con ese ID o [] si no lo encuentra
#Ejemplo: [1, 'Diego Mora', [100,99,98,100,90], 'Cartago']
def buscar_por_id (ID):
        global estudiantes
        for est in estudiantes:
                if est[0] == ID:
                        return est
        return []


#insertar estudiante
#dados los datos de un estudiante inserta en la lista y guarda en archivo
#no permite repetir IDs
def insertar_estudiante(ID, nombre, notas, provincia):
        global estudiantes
        id_buscado = buscar_por_id (ID)

        if id_buscado == []: #es [] porque no lo encontró, por tanto puede inserta
                estudiantes += [[ID, nombre, notas, provincia]]
                guardar_archivo(FILENAME, str(estudiantes))
        



#actualizar estudiante
#dado un ID, un nombre y una lista de notas, modifique el nombre y haga append
# de las notas en el estudiante del ID dado
def actualizar_estudiante(ID, nombre, notas):
        global estudiantes

        buscado = buscar_por_id (ID)
        if buscado != []:
                buscado[1] = nombre
                buscado[2] += notas  #buscado[2].expand(notas)
                guardar_archivo(FILENAME, str(estudiantes))
        
        
#eliminar estudiante
#dado un ID elimine el estudiante de la lista, si no encuentra el id
#no hace nada
def eliminar_estudiante(ID):
        global estudiantes
        buscado = buscar_por_id (ID)
        if buscado != []:
                estudiantes.remove(buscado)
                guardar_archivo(FILENAME, str(estudiantes))

def eliminar_estudiante_v2 (ID):
        global estudiantes
        res = []
        for est in estudiantes:
                if est[0] != ID:
                        res += [est]
        estudiantes = res
        guardar_archivo(FILENAME, str(estudiantes))


'''
"Si terminan"
haga una función que agregue una nota a todos los estudiantes de la lista

agregarNota(95) > a todos los estudiantes les agrega un 95 a sus notas
'''
def agregar_nota (nota):
        global estudiantes
        if nota >= 0 and nota <= 100:
                for est in estudiantes:
                        est[2] += [nota]
                guardar_archivo(FILENAME, str(estudiantes))



#cada vez que le de F5, se llama esta línea y carga el archivo a la lista
cargar_estudiantes()
