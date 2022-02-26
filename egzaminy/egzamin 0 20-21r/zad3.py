from zad3testy import runtests
from math import inf

#tworze 3 wierzchołki
#mogę użyć zwykłych, właśnie używam dwumilowych, mogę użyc dwumilowych
#jeśli uzywam dwumilowych butów to zapamiętuje parenta
#dzięki temu mogę sprawdzić która krawędz bedzie wieksza przy uzyciu
#puszczam dijkstre

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        for j in range(3):
            if not processed[i][j] and d[i][j] != inf and minimum > d[i][j] and i != v and i != j:
                minimum = d[i][j]
                ind = i

    return ind


def dijkstra(G,v):
    n = len(G)
    d = [[inf,inf,inf] for _ in range(n)]#mogę użyć zwykłych, właśnie używam dwumilowych, mogę użyc dwumilowych
    d[v][0], d[v][1], d[v][2] = 0, 0, 0

    parents = [None]*n

    processed = [[False,False,False] for _ in range(n)] #wierzchołki przetworzone

    while v is not None:
        if not processed[v][0]:
            for i in range(n):
                if G[v][i] != 0 and d[i][0] > d[v][0] + G[v][i]:
                    d[i][0] = d[v][0] + G[v][i]
                if G[v][i] != 0 and d[i][2] > d[v][0] + G[v][i]:
                    d[i][2] = d[v][0] + G[v][i]
            processed[v][0] = True
        if not processed[v][1]:
            for i in range(n):
                if G[v][i] != 0 and parents[v] is not None and d[i][0] > d[parents[v]][2] + max(G[v][i],G[parents[v]][v]):
                    d[i][0] = d[parents[v]][2] + max(G[v][i],G[parents[v]][v])
            processed[v][1] = True
        if not processed[v][2]:
            for i in range(n):
                if G[v][i] != 0 and d[i][1] > d[v][2] + G[v][i]: #sprawdzam czy opłaca mi sie użyc dwumilowych butów
                    d[i][1] = d[v][2] + G[v][i]
                    parents[i] = v
            processed[v][2] = True

        v = minimum_distance(d,n,v,processed)

    return d

def jumper(G, s, w):
    d = dijkstra(G,s)

    return min(d[w])

runtests(jumper)