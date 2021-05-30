#Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować algorytm,
#który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to takie graf H,
#że w H mamy krawędź z u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).

from math import inf

def floyd_warshall(G):
    n = len(G)

    P = [[None]*n for _ in range(n)] #poprzednik v na najkrótszej ścieżce z u do v
    S = [[inf]*n for _ in range(n)] #macierz dł. najkrótszych ścieżek używających {v1,...,vt} jako wewnętrzne

    for i in range(n):
        S[i][i] = 0

    for i in range(n): #bezposrednie krawedzie jako minimalne sciezki wyjsciowe
        for j in range(n):
            if G[i][j] != 0:
                S[i][j] = G[i][j]

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = t

    return S

def closure(G): #szukam scieżek miedzy wszystkimi wierzchołkami
    n = len(G)
    res = floyd_warshall(G)
    for i in range(n):
        for j in range(n): #jesli wystepuje sciezka to jest krawedz 1
            if res[i][j] == inf:
                res[i][j] = 0
            elif res[i][j] != 0:
                res[i][j] = 1

    return res



# [0, 1, 1, 0, 1]
# [0, 0, 1, 0, 1]
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 1]
# [0, 0, 0, 0, 0]
G = [[0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0]]

print(closure(G))