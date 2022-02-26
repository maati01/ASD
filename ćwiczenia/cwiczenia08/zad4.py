# sortuje krawędzie
# modyfikuje dfsa tak, że bierze największą możliwą która przystaje do poprzedniego wierzchołka
# reszte wiekszych pomijam bo i tak sie nie przydadzą
from math import inf


#prawdopodbnie problem ze zlożonoscią
#wydaje mi się że jest to O(V^2 + E)
#ewentualnie O((E+V)*V) XD
#wersja 4.1 jest lepsza
def DFS(G, x, edges, last):  # zmodyfikowany dfs
    n = len(G)
    visited = [False] * n
    parents = [None] * n

    def dfs_visit(u, edges, k, last):  # k to indeks dla krawedzi na ktorej skonczylem ostatnio zeby ograniczyc zlozoność
        visited[u] = True
        for v in range(len(G[u])):
            if not visited[v] and G[u][v]:
                for i in range(k, len(edges)):
                    if (G[u][v] == G[edges[i][1]][edges[i][2]] or G[u][v] == G[edges[i][2]][edges[i][1]]) and G[u][v] < last:
                        parents[v] = u
                        dfs_visit(v, edges, i + 1, G[u][v])

    dfs_visit(x, edges, 0, last)

    return parents


def get_result(parents, x, y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents, x, parents[y]) + [y]


def decreasing_edges(G, x, y):
    n = len(G)
    edges = []

    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                edges.append((G[i][j], i, j))

    edges.sort(key=lambda x: x[0], reverse=True)

    parents = DFS(G, x, edges, inf)

    if parents[y] is None:
        return False
    else:
        return get_result(parents, x, y)

# [0, 3, 4, 2]
G = [[0, 1, 0, 3, 0],
     [1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1],
     [3, 0, 0, 0, 2],
     [0, 0, 1, 2, 0]]
print(decreasing_edges(G, 0, 2))
#False
G = [[0, 1, 0, 3, 0],
     [1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1],
     [3, 0, 0, 0, 1],
     [0, 0, 1, 1, 0]]
print(decreasing_edges(G, 0, 2))
#[3, 4, 2]
G = [[0, 1, 0, 3, 0],
     [1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1],
     [3, 0, 0, 0, 2],
     [0, 0, 1, 2, 0]]
print(decreasing_edges(G, 3, 2))
