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
    "vertices": ["Aberdeen", "Edinburgh", "Fort William", "Glasgow", "Inverness", "Perth"],
    "arestas": [
        (0, 1, 120),  # Aberdeen - Edinburgh
        (0, 2, 147),  # Aberdeen - Fort William
        (0, 3, 142),  # Aberdeen - Glasgow
        (0, 4, 104),  # Aberdeen - Inverness
        (0, 5, 81),   # Aberdeen - Perth
        (1, 2, 132),  # Edinburgh - Fort William
        (1, 3, 42),   # Edinburgh - Glasgow
        (1, 4, 157),  # Edinburgh - Inverness
        (1, 5, 45),   # Edinburgh - Perth
        (2, 3, 102),  # Fort William - Glasgow
        (2, 4, 66),   # Fort William - Inverness
        (2, 5, 105),  # Fort William - Perth
        (3, 4, 168),  # Glasgow - Inverness
        (3, 5, 61),   # Glasgow - Perth
        (4, 5, 112)   # Inverness - Perth
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
