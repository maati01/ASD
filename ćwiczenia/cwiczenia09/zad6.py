from math import inf

#dijsktra O(V^2)
#duplikuje wierzchołki, żeby wiedzieć ktos ostatnio jechał i z jaką wartością
#relaksuje wartość tylko dla Alicji, bo dla niej minimalizuje dystans
#zmieniam kierowce co wierzchołek

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i][0] and d[i][0] != inf and minimum > d[i][0] and i != v:
            minimum = d[i][0]
            ind = i
        if not processed[i][1] and d[i][1] != inf and minimum > d[i][1] and i != v:
            minimum = d[i][1]
            ind = i

    return ind

def dijkstra(G,v):
    n = len(G)
    d = [[inf, inf] for _ in range(n)]
    d[v][0] = 0 #koncowy minimalny dystans
    d[v][1] = 0
    parents = [[None, None] for _ in range(n)]
    processed = [[False, False] for _ in range(n)] #wierzchołki przetworzone
    last = [[False, False] for _ in range(n)] #ostatnio prowadził/a (Alicja, Bob)
    last[v][0] = True
    last[v][1] = True

    while v is not None:
        if not processed[v][0] and last[v][0]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc, sytacja gdy ostatnio prowadziła Alicja
            for i in range(n):
                if G[v][i] != 0 and d[i][1] > d[v][0] + G[v][i]: #relaksacja
                    d[i][1] = d[v][0] #nie dodaje bo prowadzi Bob
                    parents[i][1] = v
                    last[i][1] = True
            processed[v][0] = True
        if not processed[v][1] and last[v][1]:#ostatnio porwadził Bob
            for i in range(n):
                if G[v][i] != 0 and d[i][0] > d[v][1] + G[v][i]: #relaksacja, patrze kto byl ostatni, realaksuje tylko trase dla Alicji
                    d[i][0] = d[v][1] + G[v][i] #dodaje do trasy Alicji
                    parents[i][0] = v
                    last[i][0] = True
            processed[v][1] = True

        v = minimum_distance(d,n,v,processed)

    return d,parents

def get_result(parents,x,y,ind):
    if parents[y][ind] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y][ind],1 - ind ) + [y]

def who_start(parents,x,y,ind):
    if parents[y][ind] is None:
        return ind
    else:
        return who_start(parents,x,parents[y][ind],1 - ind )


def two_drivers(G,a,b):
    d, parents = dijkstra(G, a)

    if d[b][1] >= d[b][0]:
        res = get_result(parents,a,b,0)
        ind = who_start(parents, a, b, 0)

    else:
        res = get_result(parents, a, b, 1)
        ind = who_start(parents, a, b, 1)

    if ind == 0:
        return res, 'Booooob'
    else:
        return res, 'Alicjaaa'










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

G = [[0, 5, 0, 0, 0, 2],
     [5, 0, 4, 0, 4, 1],
     [0, 4, 0, 1, 2, 0],
     [0, 0, 1, 0, 2, 0],
     [0, 4, 2, 2, 0, 3],
     [2, 1, 0, 0, 3, 0]]
print(two_drivers(G,0,4)) #([0, 1, 5, 4], 'Booooob')

G = [[0, 5, 0, 0, 0, 2],
     [5, 0, 4, 0, 4, 1],
     [0, 4, 0, 1, 2, 0],
     [0, 0, 1, 0, 2, 0],
     [0, 4, 2, 2, 0, 3],
     [2, 1, 0, 0, 3, 0]]
print(two_drivers(G,0,3)) #([0, 1, 5, 4, 3], 'Booooob')