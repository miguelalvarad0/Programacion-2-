import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx

# -------------------- ADAPTADOR: GrafoLista -> networkx --------------------
def grafo_lista_to_nx(grafo_lista):
    """
    Convierte una instancia de GrafoLista a un nx.DiGraph / nx.Graph.
    - Usa atributo 'peso' en cada arista para las etiquetas.
    - Evita duplicados cuando el grafo NO es dirigido (porque tu estructura guarda ambos sentidos).
    """
    G = nx.DiGraph() if grafo_lista.dirigido else nx.Graph()

    # Agregar nodos
    for nombre in grafo_lista.vertices:
        G.add_node(nombre)

    # Agregar aristas
    if grafo_lista.dirigido:
        # Cada tupla ya representa una arista dirigida (u -> v)
        for i, u in enumerate(grafo_lista.vertices):
            for v, p in grafo_lista.adyacencia[i]:
                G.add_edge(u, v, peso=float(p))
    else:
        # Evitar duplicados en no dirigido
        ya_agregadas = set()
        for i, u in enumerate(grafo_lista.vertices):
            for v, p in grafo_lista.adyacencia[i]:
                par = tuple(sorted((u, v)))
                if par not in ya_agregadas:
                    G.add_edge(u, v, peso=float(p))
                    ya_agregadas.add(par)

    return G

# -------------------- VENTANA DE DIBUJO --------------------
def abrir_ventana_grafo(grafo_lista):
    """
    Crea una Toplevel con el grafo dibujado.
    - Flechas si es dirigido.
    - Etiquetas de aristas = peso.
    """
    win = tk.Toplevel()
    win.title("Visualización de Grafo")

    # Figura de Matplotlib
    #fig: la figura completa (como una hoja).
    #ax: un espacio de gráficos dentro de la figura (donde dibujas el grafo, las curvas, etc.).
    fig = Figure(figsize=(6, 5))
    ax = fig.add_subplot(111)

    # Convertir el grafo
    G = grafo_lista_to_nx(grafo_lista)

    # Layout (posiciones)
    pos = nx.spring_layout(G, seed=42)  # puedes cambiar por nx.circular_layout(G)

    # Dibujar nodos y aristas
    nx.draw(
        G, pos, ax=ax, with_labels=True, node_color="lightblue",
        node_size=1300, arrows=grafo_lista.dirigido, font_size=10
    )

    # Etiquetas de aristas: mostrar 'peso'
    labels = nx.get_edge_attributes(G, "peso")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    ax.set_title("Grafo dirigido" if grafo_lista.dirigido else "Grafo no dirigido")
    ax.axis("off")

    # Embebido en Tk
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw_idle()

# -------------------- APP: ventana principal con botón --------------------
def lanzar_app(grafo_lista):
    root = tk.Tk()
    root.title("Demo GrafoLista")

    frm = ttk.Frame(root, padding=12)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="Grafo con lista de adyacencia").pack(pady=(0,8))
    ttk.Button(frm, text="Ver grafo", command=lambda: abrir_ventana_grafo(grafo_lista)).pack()

    root.mainloop()

# -------------------- EJEMPLO DE USO CON TU CLASE --------------------
if __name__ == "__main__":
    # Tu clase GrafoLista debe estar definida/importada antes de este bloque.
    class GrafoLista:
        def __init__(self, dirigido=False):
            self.dirigido = dirigido
            self.vertices = []
            self.adyacencia = []

        def _idx(self, nombre): return self.vertices.index(nombre)

        def agregar_vertice(self, nombre):
            if nombre not in self.vertices:
                self.vertices.append(nombre)
                self.adyacencia.append([])

        def agregar_arista(self, origen, destino, peso=1.0):
            self.agregar_vertice(origen)
            self.agregar_vertice(destino)
            io = self._idx(origen); idest = self._idx(destino)
            if destino not in [v for (v, _) in self.adyacencia[io]]:
                self.adyacencia[io].append((destino, float(peso)))
            if not self.dirigido:
                if origen not in [v for (v, _) in self.adyacencia[idest]]:
                    self.adyacencia[idest].append((origen, float(peso)))

    # Construimos el ejemplo del usuario (dirigido)
    g = GrafoLista(dirigido=True)
    g.agregar_arista("SanJose", "Cartago", 20.0)
    g.agregar_arista("SanJose", "Alajuela", 15.0)
    g.agregar_arista("Cartago", "Limon", 90.0)
    g.agregar_arista("Alajuela", "Heredia", 22.0)
    g.agregar_arista("Heredia", "Cartago", 18.0)

    # Lanzar UI
    lanzar_app(g)
