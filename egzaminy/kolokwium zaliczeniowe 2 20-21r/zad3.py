
#dijkstra bez kolejki priotytetowej, ma złożoność O(V^2)
#dijkstra v razy ->  O(V^3)
#tworze macierz najkrótszych sciezek miedzy wierzchołkami
#dla kazdej krawedzi o wierzchołkach i,j sprawdzam czy sciezka z s do i oraz j do t plus krawedz z i do j
#jest równa minimalnemu dystansowi między wierzchołkami s i t
#jesli tak to ta krawedz nalezy do jednej z najkrótszych ścieżek
#złożoność całego algorytmu O(V^3)
#zlożoność pamięciowa O(V^2)

from zad3testy import runtests
from math import inf

def minimum_distance(d,n,v,visited): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not visited[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind

def dijkstra(G, s):
    n = len(G)
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    v = s
    while v is not None:
        if not visited[v]:
            visited[v] = True
            for u in range(len(G[v])):
                if not visited[G[v][u][0]] and d[G[v][u][0]] > d[v] + G[v][u][1]:
                    d[G[v][u][0]] = d[v] + G[v][u][1]

        v = minimum_distance(d,n,v,visited)

    return d

def paths(G,s,t):
    n = len(G)
    S = [dijkstra(G, i) for i in range(n)]

    mindist = S[s][t]

    if mindist == inf:
        return 0

    edges = 0

    for i in range(n):
        for j in range(len(G[i])):
            if S[s][i] + G[i][j][1] + S[G[i][j][0]][t] == mindist:
                edges += 1

    return edges

runtests( paths )