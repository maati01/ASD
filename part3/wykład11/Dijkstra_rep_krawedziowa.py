from queue import PriorityQueue
from math import inf

#dijkstra dla rep krawedziowej
#sortuje
#zapisuje sb ile krawedzi i od którego indeksu w tablicy są krawędzie od wierzchołka v
#robie to co w zwykłej dijkstrze ale uzgledniam tylko krawiedzie które wychodzą z wierzchołka v i odpowiednio przesuwa w G

def dijkstra(G,v,t):
    G.sort(key=lambda x: x[0])
    n = len(G)

    max_v = -inf
    for i in range(n):
        if max_v < max(G[i][0],G[i][1]):
            max_v = max(G[i][0],G[i][1])

    cnt_v = [0]*(max_v + 1) #liczba krawedzi wychodzaca z wierzchołka v
    start_ind = [0]*(max_v + 1) #nowe wierzchołki w tablicy G
    prev = -1
    ind = 0
    flag = True
    for i in range(n):
        if v == G[i][0] and flag: #miejsce gdzie startowy wierzcholek zaczyna sie w G
            v = i
            flag = False
        cnt_v[G[i][0]] += 1
        if prev != [G[i][0]]:
            start_ind[ind] = i
            prev = [G[i][0]]
            ind += 1

    d = [inf]*(max_v + 1)
    d[G[v][0]] = 0 #koncowy minimalny dystans
    parents = [None]*(max_v + 1)
    processed = [False]*(max_v + 1) #wierzchołki przetworzone
    Q = PriorityQueue()
    Q.put((d[G[v][0]],G[v][0])) #krotka trzyma akutalny dystans i indeks
    while not Q.empty():
        temp = Q.get() #priority queue posortowane po oszacowanych dystansach
        u = temp[1]
        dist = temp[0]
        if not processed[u]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc

            for i in range(cnt_v[u]):
                if d[G[start_ind[u] + i][1]] > dist + G[start_ind[u] + i][2]: #relaksacja
                    d[G[start_ind[u] + i][1]] = dist + G[start_ind[u] + i][2]
                    parents[i] = u
                    Q.put((d[G[start_ind[u] + i][1]],G[start_ind[u] + i][1]))
            processed[u] = True

    return d[t]

G = [[0,1,1],[0,2,2],[1,3,3],[1,0,1],[2,0,2],[2,3,4],[3,1,3],[3,2,4]]
print(dijkstra(G,0,3)) #4
print(dijkstra(G,1,2)) #3
print(dijkstra(G,2,3)) #4