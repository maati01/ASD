from math import inf

#dijsktra O(V^2)
#trzymam wartosc kto ostatnio prowadził, 0 Bob, 1 Alicja
#relaksuje tylko dla drogi pokonanej przez Alicje
#puszczam dijkstre dwa razy, raz zaczyna Alicja a raz Bob

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind


def dijkstra(G,v,start):
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    if start == 'A':
        last = [0]*n
    else:
        last = [1]*n

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != 0 and d[i] > d[v] + G[v][i] and last[v] == 0: #relaksacja, patrze kto byl ostatni, realaksuje tylko trase dla Alicji
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
                    last[i] = 1
                elif G[v][i] != 0 and d[i] > d[v] + G[v][i] and last[v] == 1:
                    parents[i] = v
                    d[i] = d[v]
                    last[i] = 0

            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return d,parents

def get_result(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y]) + [y]

def two_drivers(G,a,b):
    dA, parentsA = dijkstra(G,a,'A')
    dB, parentsB = dijkstra(G,a,'B')

    if dA[b] == inf and dB[b] == inf:
        return False
    elif dA[b] == inf:
        return get_result(parentsB,a,b), 'Booooob'
    elif dB[b] == inf:
        return get_result(parentsA, a, b), 'Alicjaaa'

    if dA[b] < dB[b]:
        return get_result(parentsA, a, b), 'Alicjaaa'
    else:
        return get_result(parentsB, a, b), 'Booooob'


G = [[0,5,0,0,0,0,0,1],
     [5,0,5,0,0,0,0,0],
     [0,5,0,5,0,0,0,0],
     [0,0,5,0,5,0,0,0],
     [0,0,0,5,0,100,0,0],
     [0,0,0,0,100,0,1,0],
     [0,0,0,0,0,1,0,100],
     [1,0,0,0,0,0,100,0]]
print(two_drivers(G,0,4)) #([0, 7, 6, 5, 4], 'Alicjaaa')

G = [[0,5,0,0,0,0,0,1],
     [5,0,5,0,0,0,0,0],
     [0,5,0,5,0,0,0,0],
     [0,0,5,0,5,0,0,0],
     [0,0,0,5,0,100,0,0],
     [0,0,0,0,100,0,100,0],
     [0,0,0,0,0,100,0,100],
     [1,0,0,0,0,0,100,0]]
print(two_drivers(G,0,4)) #([0, 1, 2, 3, 4], 'Booooob')


G = [[0,5,0,0,0,0,0,1],
     [5,0,5,0,0,0,0,0],
     [0,5,0,5,0,0,0,0],
     [0,0,5,0,5,0,0,0],
     [0,0,0,5,0,100,0,0],
     [0,0,0,0,100,0,1,0],
     [0,0,0,0,0,1,0,100],
     [1,0,0,0,0,0,100,0]]
print(two_drivers(G,2,7)) #([2, 1, 0, 7], 'Booooob')

