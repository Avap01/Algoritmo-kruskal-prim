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
    "vertices": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
    "arestas": [
        (2, 4, 1),  # c - e
        (1, 4, 2),  # b - e
        (5, 6, 3),  # f - g
        (4, 10, 4), # e - k
        (9, 8, 5),  # j - i
        (8, 10, 6), # i - k
        (1, 2, 7),  # b - c
        (5, 10, 8), # f - k
        (4, 5, 9),  # e - f
        (0, 2, 10), # a - c
        (10, 11, 11), # k - l
        (0, 9, 12),  # a - j
        (1, 3, 13),  # b - d
        (8, 11, 14), # i - l
        (3, 6, 15),  # d - g
        (0, 1, 16),  # a - b
        (6, 7, 18),  # g - h
        (7, 9, 19),  # h - j
        (5, 7, 20),  # f - h
        (2, 6, 21)   # c - g
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
