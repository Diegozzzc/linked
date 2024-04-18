import networkx as nx
import matplotlib.pyplot as plt
import random

# Definición de los estados y sus costos
estados = {
    'Baja California': 100,
    'Sonora': 80,
    'Chihuahua': 120,
    'Nuevo León': 90,
    'Jalisco': 70,
    'Veracruz': 110,
    'Yucatán': 150
}

# Generar una lista aleatoria de estados sin repetición
estados_unicos = list(estados.keys())
random.shuffle(estados_unicos)
estados_elegidos = estados_unicos[:7]

# Crear el grafo
G = nx.Graph()

# Agregar los nodos (estados)
for estado in estados_elegidos:
    G.add_node(estado)

# Agregar las aristas (conexiones entre estados) con costos
for estado1 in estados_elegidos:
    for estado2 in estados_elegidos:
        if estado1 != estado2:
            costo = random.randint(50, 200)  # Costo aleatorio entre 50 y 200
            G.add_edge(estado1, estado2, weight=costo)

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de Estados de la República Mexicana")
plt.show()

# Imprimir los costos de ir a cada estado
print("Costo de ir a cada estado:")
for estado, costo in estados.items():
    print(f"{estado}: ${costo}")
