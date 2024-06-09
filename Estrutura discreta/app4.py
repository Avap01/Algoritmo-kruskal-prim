import heapq

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.V = len(vertices)
        self.indice_vertices = {vertice: indice for indice, vertice in enumerate(vertices)}
        self.grafo = []

    def adicionar_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        def unir(x, y):
            raiz_x = self.encontrar(parent, x)
            raiz_y = self.encontrar(parent, y)

            if rank[raiz_x] < rank[raiz_y]:
                parent[raiz_x] = raiz_y
            elif rank[raiz_x] > rank[raiz_y]:
                parent[raiz_y] = raiz_x
            else:
                parent[raiz_y] = raiz_x
                rank[raiz_x] += 1

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.encontrar(parent, u)
            y = self.encontrar(parent, v)

            if x != y:
                e += 1
                resultado.append([u, v, w])
                unir(x, y)

        print("Arestas na AGM usando Kruskal:")
        for u, v, peso in sorted(resultado, key=lambda item: (item[0], item[1])):
            print(f"{self.vertices[u]} -- {self.vertices[v]} == {peso}")

    def prim(self):
        visitado = [False] * self.V
        arestas = [(0, 0)]  # Peso, nó inicial
        mst = []

        while arestas:
            peso, u = heapq.heappop(arestas)
            if not visitado[u]:
                visitado[u] = True
                mst.append((peso, u))

                for v, w in [(v, w) for x, v, w in self.grafo if x == u] + [(x, w) for x, v, w in self.grafo if v == u]:
                    if not visitado[v]:
                        heapq.heappush(arestas, (w, v))

        print("\nArestas na AGM usando Prim:")
        for peso, u in mst[1:]:
            print(f"{self.vertices[u]} com peso {peso}")

# Dados do grafo
grafo = {
    "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    "arestas": [
        (0, 1, 15), # A - B
        (0, 2, 10), #,A - C
        (0, 3, 19), # A - D
        (1, 3, 7), # B - D
        (1, 4, 17), # B - E
        (2, 5, 14) ,# C - F
        (3, 4, 12), # D - E
        (3, 5, 16), # D - F
        (3, 6, 20), # D - G
        (4, 6, 20), # E - G
        (4, 8, 20), # E - I
        (4, 9, 13), # E - J
        (5, 6, 9), # F - G
        (5, 7, 9), # F - H
        (5, 9, 5) ,# F - J
        (6, 7, 4) ,# G - H
        (6, 8, 11), # G - I
        (7, 8, 20), # H - I
        (7, 9, 8), # H - J
        (8, 9, 18) # I - J
    ]
}

# Criando o grafo
g = Grafo(grafo["vertices"])
for aresta in grafo["arestas"]:
    u, v, peso = aresta
    g.adicionar_aresta(u, v, peso)

print("Algoritmo de Kruskal:")
g.kruskal()

print("\nAlgoritmo de Prim:")
g.prim()
