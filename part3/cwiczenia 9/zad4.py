from math import log2
from math import inf
from math import pow
#zamieniam wszystkie krawedzie na logarytmy
#log(a*b*c) = log(a) + log(b) + log(c)
#dzieki temu moge wykonac relaksacje na krawedziach i wynik otrzymam o najmniejszym iloczynie
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
    real_d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    real_d[v] = 0
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i][1] != 0 and d[i] > d[v] + G[v][i][0]: #relaksacja dla krawedzi roznych od zera, po logarytmowaniu moga byc rowne zero
                    d[i] = d[v] + G[v][i][0]
                    real_d[i] = real_d[v] + G[v][i][1]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return parents,d, real_d

def get_result(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y]) + [y]

def min_product(G,u,v):
    n = len(G)

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i][j] = (log2(G[i][j]), G[i][j])
            else:
                G[i][j] = (0, 0)

    parents, d, real_d = dijkstra(G,u)

    if parents[v] is None:
        return False
    else:
        return get_result(parents,u,v), pow(d[v],2), real_d[v]

G =[[0,1,0,0,0,0,0,2],
    [1,0,1,0,0,0,0,0],
    [0,1,0,2,0,0,0,0],
    [0,0,2,0,2,0,0,0],
    [0,0,0,2,0,1,0,0],
    [0,0,0,0,1,0,2,0],
    [0,0,0,0,0,2,0,2],
    [2,0,0,0,0,0,2,0]]
print(min_product(G,0,5)) #([0, 1, 2, 3, 4, 5], 2.0, 7) , ścieżka, iloczyn, suma

G =[[0,1,0,0,0,0,0,2],
    [1,0,1,0,0,0,0,0],
    [0,1,0,2,0,0,0,0],
    [0,0,2,0,2,0,0,0],
    [0,0,0,2,0,1,0,0],
    [0,0,0,0,1,0,2,0],
    [0,0,0,0,0,2,0,2],
    [2,0,0,0,0,0,2,0]]
print(min_product(G,2,6)) #([2, 1, 0, 7, 6], 4.0, 6)
