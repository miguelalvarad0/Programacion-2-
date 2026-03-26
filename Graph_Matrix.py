class Grafo_Matriz:
        def __init__(self):
                self.matriz = []
                self.nombres = [] # lista de nombres, el indice del nombre determina la fila y columna de ese vertice

        #inserta un nuevo vértice, creando una fila y columna nuevas
        #retorna el indice donde se encuentra el vértice
        def insertar_vertice (self, nombre):
                #validar que no exista el vértice
                if nombre in self.nombres:
                        return self.nombre.index(nombre)

                self.nombres.append(nombre) #inserta el nuevo nombre en la lista de etiquetas
                n = len(self.nombres) #averigua la dimension nxn de la matriz cuadrada

                #agregar la nueva fila del final
                self.matriz.append([0] * n)
                #agregar columna nueva: a cada fila agregar un nuevo elemento 0 al final
                for i in range(n-1):
                        self.matriz[i].append(0)


        # insertar arista: busca el indice del origen y destino y pone el peso en ese fila, columna
        # si el origen o destino no existen los va a insertar(crear como vertices antes)
        def insertar_arista(self, nombre_origen, nombre_destino, peso = 1):
                if nombre_origen not in self.nombres:
                        self.insertar_vertice(nombre_origen)
                if nombre_destino not in self.nombres:
                        self.insertar_vertice(nombre_destino)
                #averiguar los indices de los nombres
                i = self.nombres.index(nombre_origen)
                j = self.nombres.index(nombre_destino)

                self.matriz[i][j] = peso
                self.matriz[j][i] = peso #cuando es no dirigido


        #elimina el camino (arista) entre origen y destino
        def eliminar_arista(self, nombre_origen, nombre_destino):
                if nombre_origen in self.nombres and nombre_destino in self.nombres:
                        #averiguar los indices de los nombres
                        i = self.nombres.index(nombre_origen)
                        j= self.nombres.index(nombre_destino)
                        self.matriz[i][j] = 0
                        self.matriz[j][i] = 0 #cuando es no dirigido

        #elimina la fila y columna del vértice con el nombre dado
        def eliminar_vertice(self, nombre):
                if nombre not in self.nombres:  #valida que el nombre exista
                        return
                #averigua el indice del nombre que sí está
                index = self.nombres.index(nombre)
                #elimina fila de vertice
                self.matriz.pop(index)
                #para cada fila, elimina la columma index
                for fila in self.matriz:
                        fila.pop(index)
                #eliminar
                self.nombres.pop(index)
                
                
                        
             
        #print de la matriz del grafo
        def mostrar(self):
                print(' ', end  = "\t")
                for nombre in self.nombres:
                        print(nombre, end = "\t")
                print()
                for i in range(len(self.nombres)):
                        print(self.nombres[i], end  = "\t")
                        for j in range(len(self.nombres)):
                                print(self.matriz[i][j], end  = "\t")
                        print()
                                        
        def convertir_a_lista(self):
            from GrafoListaAdyancencia import GrafoLista  # importa tu clase de lista

            grafo_lista = GrafoLista()

            # insertar todos los vértices
            for v in self.nombres:
                grafo_lista.agregar_vertice(v)

            # recorrer la matriz y añadir las aristas
            n = len(self.nombres)
            for i in range(n):
                for j in range(i+1, n):  # para no repetir aristas
                    peso = self.matriz[i][j]
                    if peso != 0:
                        origen = self.nombres[i]
                        destino = self.nombres[j]
                        grafo_lista.agregar_arista(origen, destino, peso)

            return grafo_lista

# Examen: Calcular grados de los nodos en un grafo dirigido

        def calcular_grados(matriz):
            """
            Calcula el in-degree y out-degree de cada nodo en un grafo dirigido
            representado con matriz de adyacencia.
            """
            n = len(matriz)  # número de nodos
            nodos = [chr(65 + i) for i in range(n)]  # A, B, C, ...

            for i in range(n):
                in_degree = 0
                out_degree = 0

                # TODO: Calcular out-degree (aristas que salen de i)

                # TODO: Calcular in-degree (aristas que llegan a i)

                # TODO: Imprimir el resultado para el nodo i

if __name__ == "__main__":
        grafo = Grafo_Matriz()  # crea el objeto y lo referencia con grafo
        grafo.insertar_vertice('A')
        grafo.insertar_vertice('B')
        grafo.insertar_vertice('C')

        grafo.insertar_arista('A', 'D', 20)
        grafo.insertar_arista('E', 'B', 22)
        grafo.insertar_arista('A', 'B', 25)
        grafo.insertar_arista('A', 'C', 60)
        grafo.insertar_arista('C', 'D', 27)

        #grafo.mostrar()
        #print()
        #grafo.eliminar_arista('A', 'C')
        #grafo.mostrar()
        #print()
        #grafo.eliminar_vertice('C')
        #grafo.mostrar()
        #print()

        from GrafoListaAdyancencia import GrafoLista
        print('QUIZ Matriz a Lista---------------------------------------')
        print('Matriz')
        grafo.mostrar()
        print()
        print('Lista')
        grafo_lista = grafo.convertir_a_lista()
        grafo_lista.mostrar()
        print('QUIZ Matriz a Lista ---------------------------------------')
