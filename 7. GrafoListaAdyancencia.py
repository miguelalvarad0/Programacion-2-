

'''
vertices ['A', 'B', 'C','D']
adyacencia [[('B', 0), ('C', 10), ('D',30)], [('A',50)],  [('A',8)],[('A',30)] ]
dirigido = False
'''

class GrafoLista:
        def __init__(self, dirigido=False):
                self.dirigido = dirigido
                self.vertices = [] #las etiquetas de los vertices y determina el indice
                self.adyacencia=[] #[[('B', 50), ('C', 10)], [('A',50)],  [('A',8)] ]

        #--utilitarios
        # Utilizar para obtener el índice de un vértice, y con el index lograr adyacencia[index] para obtener las arista del vertice       
        def _idx(self, nombre): #recibe el nombre del vértice para obtener el indice donde se encuentra
                return self.vertices.index(nombre)

        #dado un vertice y el indice de una lista de aristas, retorna True si el nombre está en la lista dada
        def _esta_arista(self, nombre, index_lista):
                #return nombre not in [v for (v, _) in self.adyacencia[index_lista]]
                for arista in self.adyacencia[index_lista]:
                        if arista[0] == nombre: #si el nombre en la tupla es igual al buscado
                                return True
                return False
                

        def agregar_vertice(self, nombre):
                if nombre not in self.vertices:
                        self.vertices.append(nombre)
                        self.adyacencia.append([])

        def agregar_arista(self, origen, destino, peso = 1.0):
                #si no existen los vertices se crean
                self.agregar_vertice(origen)
                self.agregar_vertice(destino)
                #averiguar indices de origen y destino
                index_origen = self._idx(origen)
                index_destino= self._idx(destino)
                #insertamos en lista origen
                #validar que no se repita la arista
                if not self._esta_arista(destino, index_origen):
                        self.adyacencia[index_origen].append((destino, peso))
                #si no es dirigido, se inserta en lista destino
                if not self.dirigido:  #self.dirigido == False
                        if not self._esta_arista(origen, index_destino):
                                self.adyacencia[index_destino].append((origen, peso))


        def mostrar(self):
                for i in range(0,len(self.vertices)):
                        print (self.vertices[i], end=' -> ')
                        for n,p in self.adyacencia[i]:   #(nombre,peso)
                                print (f"{n}({p})", end='\t')   #print(n,"(",p,")\t")
                        print()

        def eliminar_arista(self, origen, destino):
                #validar que existen los vertices
                if origen in self.vertices and destino in self.vertices:
                        #averiguar indices de origen y destino
                        index_origen = self._idx(origen)
                        index_destino= self._idx(destino)
                        self.adyacencia[index_origen] = [ (v,p) for (v,p) in self.adyacencia[index_origen] if v != destino ]
                        #si es no dirigido
                        if not self.dirigido:
                                self.adyacencia[index_destino] = [ (v,p) for (v,p) in self.adyacencia[index_destino] if v != origen ]
                                
                        

                        
        #eliminar un vertice y las aristas del vertice y todas las aristas que llegaban a ese vertice
        def eliminar_vertice(self, nombre):
                #verificar existe
                if nombre not in self.vertices:
                        return
                #buscar el indice
                index = self._idx(nombre)
                #quitar la lista de adyancencia del indice
                self.adyacencia.pop(index)
                #quitar todas las aristas que tenían como referencia el vertice
                for i in range(len(self.adyacencia)):
                        self.adyacencia[i] = [ (v,p) for (v,p) in self.adyacencia[i] if v != nombre ]
                #quitamos el vértice de la lista de vértices
                self.vertices.pop(index)
                
                        
                

        




#TESTING
grafo = GrafoLista(False)
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_arista('A', 'B', 10)
grafo.agregar_arista('A', 'C', 11)
grafo.agregar_arista('A', 'D', 12)
grafo.agregar_arista('A', 'Z', 13)
grafo.agregar_arista('B', 'C', 13)
grafo.agregar_arista('Y', 'C', 14)
grafo.agregar_arista('Y', 'A', 15)
grafo.agregar_arista('B', 'A', 67)
#print (grafo.vertices)
#print (grafo.adyacencia)
grafo.mostrar()
print()
#grafo.eliminar_arista('A','B')
grafo.eliminar_vertice('B')
grafo.mostrar()
print()




        
        
        
