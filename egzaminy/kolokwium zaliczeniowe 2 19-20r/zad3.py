from zad3testy import runtests
from math import inf

#tworze graf z warunkami zadania
#dijkstra

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind


def dijkstra(G,v):
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != 0 and d[i] > d[v] + G[v][i]: #relaksacja
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return d

def check(val1,val2): #funckja sprawdza czy wystepuje jedna cyfra wspólna
    counter = [0]*10

    while val1 > 0:
        digit = val1%10
        counter[digit] += 1
        val1 //= 10

    while val2 > 0:
        digit = val2%10
        if counter[digit] != 0:
            return True
        val2 //= 10

    return False

def find_cost(P):
    n = len(P)

    G = [[0]*n for _ in range(n)]

    min_val = inf
    max_val = -inf
    min_ind = 0
    max_ind = 0

    for i in range(n):
        if min_val > P[i]:
            min_val = P[i]
            min_ind = i
        if max_val < P[i]:
            max_val = P[i]
            max_ind = i

    for i in range(n):
        for j in range(n):
            if i != j and check(P[i], P[j]):
                G[i][j] = abs(P[i] - P[j])

    d = dijkstra(G,min_ind)

    if d[max_ind] == inf:
        return -1
    else:
        return d[max_ind]

runtests(find_cost)