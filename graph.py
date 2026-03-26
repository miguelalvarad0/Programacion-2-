import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar nodos y aristas con pesos
'''G.add_edge("SanJose", "Cartago", km=20)
G.add_edge("SanJose", "Alajuela", km=15)
G.add_edge("Cartago", "Limon", km=90)
G.add_edge("Heredia", "Cartago", km=18)
G.add_edge("Alajuela", "Heredia", km=22)'''

G.add_edge("SanJose", "Cartago", km=20, huecos=200)
G.add_edge("SanJose", "Alajuela", km=15, huecos=230)
G.add_edge("Cartago", "Limon", km=90, huecos=240)
G.add_edge("Heredia", "Cartago", km=18, huecos=200)
G.add_edge("Alajuela", "Heredia", km=22, huecos=250)

# Posiciones automáticas
pos = nx.spring_layout(G, seed=42)
#pos = nx.circular_layout(G)

# Camino que queremos resaltar
camino = ["SanJose", "Cartago", "Limon"]
aristas_camino = list(zip(camino, camino[1:]))

# Dibujar todos los nodos y aristas
nx.draw(G, pos, with_labels=True, node_color="red", node_size=2000, arrows=True)

# Etiquetas de pesos
labels = nx.get_edge_attributes(G, 'huecos')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Dibujar aristas del camino resaltadas
nx.draw_networkx_edges(
    G, pos,
    edgelist=aristas_camino,
    edge_color="red",
    width=1
)

plt.title("Camino resaltado en rojo")
plt.show()
