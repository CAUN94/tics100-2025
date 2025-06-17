"""
📍 Algoritmos: Dijkstra y A*
Comparación de caminos más cortos sobre un grafo con pesos.
"""

import networkx as nx
import matplotlib.pyplot as plt

# 1. Crear grafo no dirigido con pesos
G = nx.Graph()
edges = [
    ('A','B',4), ('A','C',2), ('B','C',1), ('B','D',5),
    ('C','D',8), ('C','E',10), ('D','E',2), ('D','F',6),
    ('E','G',3), ('F','G',1)
]
G.add_weighted_edges_from(edges)

# 2. Posiciones fijas para reproducibilidad
pos = nx.spring_layout(G, seed=42)

# 3. Ruta más corta con Dijkstra
ruta_dijkstra = nx.shortest_path(G, source='A', target='G', weight='weight')
distancia_dijkstra = nx.shortest_path_length(G, source='A', target='G', weight='weight')
print("🔹 Ruta más corta A→G (Dijkstra):", ruta_dijkstra, "con distancia total:", distancia_dijkstra)

# 4. Ruta con A* (heurística nula, por lo que es igual a Dijkstra)
def heuristica(u, v): return 0
ruta_astar = nx.astar_path(G, source='A', target='G', heuristic=heuristica, weight='weight')
print("🔸 Ruta A* A→G:", ruta_astar)

# 5. Visualización con ruta Dijkstra resaltada
ruta_edges = list(zip(ruta_dijkstra[:-1], ruta_dijkstra[1:]))

plt.figure(figsize=(10, 7))

# Grafo base
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
        node_size=800, font_weight='bold', width=1)

# Etiquetas de pesos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Aristas en ruta más corta en rojo
nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='red', width=3)

# Nodos de la ruta más corta con borde rojo
nx.draw_networkx_nodes(
    G, pos,
    nodelist=ruta_dijkstra,
    node_color='lightblue',
    edgecolors='red',
    node_size=800,
    linewidths=2
)

plt.title("📍 Ruta más corta (A → G) resaltada en rojo con Dijkstra")
plt.axis('off')
plt.show()

# 6. Grafo dirigido para flujo máximo (ejemplo adicional)
Gflow = nx.DiGraph()
Gflow.add_edge('s', 'a', capacity=4)
Gflow.add_edge('s', 'b', capacity=3)
Gflow.add_edge('a', 'c', capacity=3)
Gflow.add_edge('b', 'c', capacity=2)
Gflow.add_edge('b', 'd', capacity=3)
Gflow.add_edge('c', 't', capacity=4)
Gflow.add_edge('d', 't', capacity=2)
flow_value, flow_dict = nx.maximum_flow(Gflow, 's', 't')
print("💧 Flujo máximo s→t:", flow_value)
print("Detalle flujo:", flow_dict)

# 7. Componentes conexas
conexas = list(nx.connected_components(G))
print("🧩 Componentes conexas:", conexas)

# 8. Detección de ciclos
try:
    ciclo = nx.find_cycle(G)
    print("♻️ Ciclo encontrado:", ciclo)
except nx.NetworkXNoCycle:
    print("✅ No hay ciclos en el grafo.")
