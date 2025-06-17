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

# 2. Visualizar el grafo
pos = nx.spring_layout(G, seed=42)  # disposición reproducible
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Red de ciudades con distancias")
plt.show()

# 3. Calcular ruta más corta A → G (Dijkstra)
ruta = nx.shortest_path(G, source='A', target='G', weight='weight')
distancia = nx.shortest_path_length(G, source='A', target='G', weight='weight')
print("🔹 Ruta más corta A→G (Dijkstra):", ruta, "con distancia total:", distancia)

# 4. Ruta usando A* con heurística h=0 (equivalente a Dijkstra)
def heuristica(u, v):
    return 0
ruta_astar = nx.astar_path(G, source='A', target='G', heuristic=heuristica, weight='weight')
print("🔸 Ruta A* A→G:", ruta_astar)

# 5. Grafo dirigido para flujo máximo (Ej: red de agua)
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

# 6. Componentes conexas
conexas = list(nx.connected_components(G))
print("🧩 Componentes conexas:", conexas)

# 7. Detección de ciclos
try:
    ciclo = nx.find_cycle(G)
    print("♻️ Ciclo encontrado:", ciclo)
except nx.NetworkXNoCycle:
    print("✅ No hay ciclos en el grafo.")
