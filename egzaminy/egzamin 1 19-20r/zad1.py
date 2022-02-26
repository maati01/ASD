from zad1testy import runtests
from math import inf


def minimum_distance(d, n, v, processed):  # funkcja szuka minimalnego dystansu
    ind = None, None
    minimum = inf
    for i in range(n):
        for j in range(3):
            if not processed[i][j] and d[i][j] != inf and minimum > d[i][j] and i != v:
                minimum = d[i][j]
                ind = i, j
    return ind[0], ind[1]


def dijkstra(G, v):
    n = len(G)
    d = [[inf, inf, inf] for _ in range(n)]
    d[v][0] = 0  # koncowy minimalny dystans
    d[v][1] = 0
    d[v][2] = 0
    processed = [[False, False, False] for _ in range(n)]  # wierzchołki przetworzone
    ind = 0

    while v is not None:
        if not processed[v][ind]:  # sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                for j in range(3):
                    if G[v][i] != 0 and d[i][j] > d[v][j] + G[v][i] and ind != j:  # relaksacja, musze zmienic srodek transportu
                        d[i][j] = d[v][j] + G[v][i]
                processed[v][ind] = True

        v, ind = minimum_distance(d, n, v, processed)

    return d


def islands(G, A, B):
    d = dijkstra(G, A)
    if d[B] == inf:
        return None
    else:
        return min(d[B])


runtests(islands)
