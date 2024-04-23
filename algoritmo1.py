import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]

    def min_distance(self, distancia, conjunto_cerrado):
        min = sys.maxsize
        for v in range(self.V):
            if distancia[v] < min and conjunto_cerrado[v] == False:
                min = distancia[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        distancia = [sys.maxsize] * self.V
        distancia[src] = 0
        conjunto_cerrado = [False] * self.V

        for cout in range(self.V):
            u = self.min_distance(distancia, conjunto_cerrado)
            conjunto_cerrado[u] = True
            for v in range(self.V):
                if self.grafo[u][v] > 0 and conjunto_cerrado[v] == False and distancia[v] > distancia[u] + self.grafo[u][v]:
                    distancia[v] = distancia[u] + self.grafo[u][v]

        self.imprimir_solucion(distancia)

    def imprimir_solucion(self, distancia):
        print("Distancia desde el nodo fuente:")
        for nodo in range(self.V):
            print(nodo, " - ", distancia[nodo])



g = Grafo(9)
g.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)
