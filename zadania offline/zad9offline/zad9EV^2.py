from queue import PriorityQueue
from math import inf

def dijkstra(G,v): #z wikipiedii
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone
    distance = [inf]*n #oszacowane dystanse
    distance[v] = 0
    Q = PriorityQueue()
    Q.put((distance[v],v)) #krotka trzyma akutalny dystans i indeks
    while not Q.empty():
        temp = Q.get() #priority queue posortowane po oszacowanych dystansach
        u = temp[1]
        distance[u] = temp[0]
        if not processed[u]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[u][i] != -1 and d[i] > d[u] + G[u][i]: #relaksacja
                    d[i] = d[u] + G[u][i]
                    parents[i] = u
                    distance[i] = d[i]
                    Q.put((distance[i],i))
            processed[u] = True

    return d,parents

def min_cycle(G):
    n = len(G)
    result = []
    min = inf
    edeges = [] #trzymam krawedzie jako krotki z waga


    for i in range(n):
        for j in range(i + 1,n):
            if G[i][j] != -1:
                edeges.append((i,j,G[i][j]))

    for e in edeges:
        temp = e[2]
        G[e[0]][e[1]] = G[e[1]][e[0]] = -1 #usuwam krawędź
        d,parents = dijkstra(G,e[0])
        if d[e[1]] != inf and d[e[1]] + e[2] < min:
            min = d[e[1]] + e[2]
            res_parents = parents
            x,y = e[0],e[1]

        G[e[0]][e[1]] = G[e[1]][e[0]] = temp #przywracam krawędź

    if min != inf:
        result.append(y)

        while y != x:
            result.append(res_parents[y])
            y = res_parents[y]


    return result,min






G = [[-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]

G = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]

print(min_cycle(G))
