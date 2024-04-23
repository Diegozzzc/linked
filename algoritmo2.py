INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    next_hop = [[None if i == j or graph[i][j] == 0 else j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_hop[i][j] = next_hop[i][k]

    return dist, next_hop

def print_path(start, end, next_hop):
    path = [start]
    while next_hop[start][end] is not None:
        start = next_hop[start][end]
        path.append(start)
    return ' -> '.join(map(str, path))

def print_shortest_paths(distances, next_hop):
    n = len(distances)
    for i in range(n):
        for j in range(n):
            if i != j:
                print(f"Distancia más corta de {i} a {j}: {distances[i][j]}")
                print(f"Camino más corto de {i} a {j}: {print_path(i, j, next_hop)}")
                print()

# Ejemplo de grafo
graph = [
    [0, 5, 0, 10, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0]
]

distances, next_hop = floyd_warshall(graph)
print("Matriz de distancias más cortas entre todos los pares de vértices:")
for row in distances:
    print(row)
print()

print("Camino más corto entre todos los pares de vértices:")
print_shortest_paths(distances, next_hop)
