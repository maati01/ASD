from math import inf

#najkrótsze ścieżki miedzy każdą parą wierzchołków
#dziala dla ujemnych krawędzi


def floyd_warshall(G):
    n = len(G)

    P = [[None]*n for _ in range(n)] #poprzednik v na najkrótszej ścieżce z u do v,parents
    S = [[inf]*n for _ in range(n)] #macierz dł. najkrótszych ścieżek używających {v1,...,vt} jako wewnętrzne

    for i in range(n):
        S[i][i] = 0

    for i in range(n): #bezposrednie krawedzie jako minimalne sciezki wyjsciowe
        for j in range(n):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
                P[i][j] = i

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]

    return S


# [0, 5, 5, 7, 9, 8]
G = [[0, 0, 10, 0, 0, 8],
    [0, 0, 0, 2, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, -2, 0, 0, 0],
    [0, -4, 0, -1, 0, 0],
    [0, 0, 0, 0, 1, 0]]

# [0, -1, -2, 0]
# [4, 0, 2, 4]
# [5, 1, 0, 2]
# [3, -1, 1, 0]
G = [[0, 0, -2, 0],
    [4, 0, 3, 0],
    [0, 0, 0, 2],
    [0, -1, 0, 0]]
G = [[0, 9, 0, 0, 0, 0, 0],
         [9, 0, 10, 0, 0, 0, 8],
         [0, 10, 0, 4, 0, 0, 0],
         [0, 0, 4, 0, 5, 0, 0],
         [0, 0, 0, 5, 0, 6, 0],
         [0, 0, 0, 0, 6, 0, 7],
         [0, 8, 0, 0, 0, 7, 0]]

G = [[0,1,2],[1,0,1],[2,1,0]]
print(floyd_warshall(G))