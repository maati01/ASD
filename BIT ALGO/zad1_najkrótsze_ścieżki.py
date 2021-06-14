from math import inf

#dijsktra O(V^2)

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu od wierzchołka v
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and minimum > min(d[i][0],d[i][1],d[i][2]) and i != v:
            minimum = min(d[i][0],d[i][1],d[i][2])
            ind = i

    return ind


def dijkstra(G,v): #zmodyfikowana dijkstra pod zadanie
    n = len(G)
    d = [[inf,inf,inf] for _ in range(n)] #1,5,8 krotka o dystanie, aktualizowana po wartości krawędzi którą weszliśmy
    d[v] = [0,0,0] #koncowy minimalny dystans z wierzchołka v
    parents = [[None,None,None] for _ in range(n)] #krawędz którą weszliśmy
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != 0: #badam przypadki w zaleznosci od obecnego kosztu na krawedzi, 3 różne przypadki
                    if parents[v][0] != G[v][i] and d[i][0] > min(d[v][1],d[v][2]) + G[v][i]:  # relaksacja z warunkiem z zadania
                        d[i][0] = min(d[v][1],d[v][2]) + G[v][i]
                        parents[i][0] = G[v][i]

                    if parents[v][1] != G[v][i] and d[i][1] > min(d[v][0], d[v][2]) + G[v][i]:
                        d[i][1] = min(d[v][0], d[v][2]) + G[v][i]
                        parents[i][1] = G[v][i]

                    if parents[v][2] != G[v][i] and d[i][1] > min(d[v][0], d[v][1]) + G[v][i]:
                        d[i][2] = min(d[v][0], d[v][1]) + G[v][i]
                        parents[i][2] = G[v][i]

            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return d

def islands(G,A,B):
    d = dijkstra(G,A)
    print(d)
    if min(d[B][0],d[B][1],d[B][2]) == inf:
        return None
    else:
        return min(d[B][0],d[B][1],d[B][2])

#5 -> 2 = 13
G = [[0,5,1,8,0,0,0],
     [5,0,0,1,0,8,0],
     [1,0,0,8,0,0,8],
     [8,1,8,0,5,0,1],
     [0,0,0,5,0,1,0],
     [0,8,0,0,1,0,5],
     [0,0,8,1,0,5,0]]

print(islands(G,5,2))