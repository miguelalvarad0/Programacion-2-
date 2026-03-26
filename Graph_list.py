class Grafo_Lista:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = []          # lista de nombres
        self.adyacencia = []        # lista de listas: en i vive [(nombre_vecino, peso), ...]

    # ---------- utilitarios ----------
    def _idx(self, nombre):
        return self.vertices.index(nombre)

    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices.append(nombre)
            self.adyacencia.append([])
        else:
            # Si ya existe, no duplicar; útil para flujos que agregan al vuelo
            pass

    def agregar_arista(self, origen, destino, peso=1.0):
        # crea vértices si no existían
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        io = self._idx(origen)
        idest = self._idx(destino)

        # evitar duplicados: comprobamos por nombre
        if destino not in [v for (v, _) in self.adyacencia[io]]:
            self.adyacencia[io].append((destino, float(peso)))

        if not self.dirigido:
            if origen not in [v for (v, _) in self.adyacencia[idest]]:
                self.adyacencia[idest].append((origen, float(peso)))

    def eliminar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            io = self._idx(origen)
            idest = self._idx(destino)
            self.adyacencia[io] = [(v, p) for (v, p) in self.adyacencia[io] if v != destino]
            if not self.dirigido:
                self.adyacencia[idest] = [(v, p) for (v, p) in self.adyacencia[idest] if v != origen]

    def eliminar_vertice(self, nombre):
        if nombre not in self.vertices:
            return
        i = self._idx(nombre)
        # quita lista propia
        self.adyacencia.pop(i)
        # quita referencias en los demás
        for lst in self.adyacencia:
            lst[:] = [(v, p) for (v, p) in lst if v != nombre]
        # quita el nombre
        self.vertices.pop(i)

    def mostrar(self):
        for i, u in enumerate(self.vertices):
            vecs = ", ".join(f"{v}({p})" for (v, p) in self.adyacencia[i])
            print(f"{u} -> {vecs}")

    # ---------- BFS ----------
    def bfs(self, origen):
        if origen not in self.vertices:
            return []
        visitados = set([origen])
        orden = []
        from collections import deque
        q = deque([origen])

        while q:
            u = q.popleft()
            orden.append(u)
            iu = self._idx(u)
            for v, _ in self.adyacencia[iu]:
                if v not in visitados:
                    visitados.add(v)
                    q.append(v)
        return orden

    # ---------- DFS ----------
    def dfs(self, origen):
        if origen not in self.vertices:
            return []
        visitados = set()
        orden = []

        def rec(u):
            visitados.add(u)
            orden.append(u)
            iu = self._idx(u)
            for v, _ in self.adyacencia[iu]:
                if v not in visitados:
                    rec(v)

        rec(origen)
        return orden

    # ---------- Dijkstra (sin heap, solo listas) ----------
    # Calcula distancias mínimas desde 'origen' y, si se da 'destino', reconstruye el camino.
    # Requiere pesos no negativos.
    def dijkstra(self, origen, destino=None):
        if origen not in self.vertices:
            return ([], [], []) if destino is not None else ([], [])
        n = len(self.vertices)
        INF = float('inf')

        # vectores alineados por índice
        dist = [INF] * n            # distancia acumulada
        prev = [None] * n           # predecesor por nombre
        visitado = [False] * n

        io = self._idx(origen)
        dist[io] = 0.0

        # conjunto de no visitados: manejado por banderas y min lineal
        for _ in range(n):
            # seleccionar u no visitado con menor dist
            u_idx = -1
            u_min = INF
            for i in range(n):
                if not visitado[i] and dist[i] < u_min:
                    u_min = dist[i]
                    u_idx = i
            if u_idx == -1:  # quedan inaccesibles
                break

            visitado[u_idx] = True
            u = self.vertices[u_idx]

            # relajar vecinos de u
            for v, w in self.adyacencia[u_idx]:
                v_idx = self._idx(v)
                if not visitado[v_idx]:
                    nd = dist[u_idx] + float(w)
                    if nd < dist[v_idx]:
                        dist[v_idx] = nd
                        prev[v_idx] = u  # guardo el nombre del predecesor

        if destino is None:
            # devolver pares (nombre, distancia)
            return [ (self.vertices[i], dist[i]) for i in range(n) ], prev

        # reconstrucción de camino a destino
        if destino not in self.vertices:
            return [], dist, prev

        camino = []
        cur = destino
        while cur is not None:
            camino.append(cur)
            cur = prev[self._idx(cur)]
        camino.reverse()

        # si el origen no alcanza al destino, el primer nodo del camino no será 'origen'
        if not camino or camino[0] != origen:
            camino = []  # sin ruta

        return camino, dist, prev

    def convertir_a_matriz(self):
        from GrafoMatriz import Grafo_Matriz  # importa tu clase de matriz

        grafo_matriz = Grafo_Matriz()

        # insertar todos los vértices
        for v in self.vertices:
            grafo_matriz.insertar_vertice(v)

        # recorrer las aristas de la lista y añadirlas a la matriz
        for i in range(len(self.adyacencia)):
            for destino, peso in self.adyacencia[i]:
                grafo_matriz.insertar_arista(self.vertices[i], destino, peso)

        return grafo_matriz


g = Grafo_Lista(dirigido=True)   # usa False si lo quieres no dirigido
g.agregar_arista("SanJose", "Cartago", 20)
g.agregar_arista("SanJose", "Alajuela", 15)
g.agregar_arista("Heredia",  "Cartago", 18)
g.agregar_arista("Alajuela", "Heredia", 22)
g.agregar_arista("Cartago",  "Limon",   90)

g.mostrar()
print("BFS desde SanJose:", g.bfs("SanJose"))
print("DFS desde SanJose:", g.dfs("SanJose"))

camino, dist, prev = g.dijkstra("SanJose", "Limon")
print("Camino mínimo SanJose→Limon:", camino)
# Todas las distancias desde SanJose:
todos, _prev = g.dijkstra("SanJose")  # devuelve lista (nombre, dist)
print("Distancias desde SanJose:", todos)

print()
from GrafoMatriz import Grafo_Matriz
grafo_matriz = g.convertir_a_matriz()
grafo_matriz.mostrar()