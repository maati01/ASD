from queue import PriorityQueue
from math import inf
from math import ceil

#zmodyfikowana dijkstra
#używam dijkstry dla reprezentacji krawedziowej
#zamiast relaksacji biore minimum z krawedzi oraz przepływu do wierzchołka u
#to mi gwarantuje najwiekszy przepływ w wierzchołku i
#do kolejki wrzucam z minusem bo szukam najwiekszego przepływu

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

    d = [-inf]*(max_v + 1)
    d[G[v][0]] = inf #koncowy minimalny dystans
    parents = [None]*(max_v + 1)
    processed = [False]*(max_v + 1) #wierzchołki przetworzone
    Q = PriorityQueue()
    Q.put((-d[G[v][0]],G[v][0])) #krotka trzyma akutalny dystans i indeks
    while not Q.empty():
        temp = Q.get() #priority queue posortowane po oszacowanych dystansach
        u = temp[1]
        dist = -temp[0]
        if not processed[u]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(cnt_v[u]):
                if d[G[start_ind[u] + i][1]] < min(dist, G[start_ind[u] + i][2]): #relaksacja zmodyfikowana
                    d[G[start_ind[u] + i][1]] = min(dist, G[start_ind[u] + i][2])
                    parents[G[start_ind[u] + i][1]] = u
                    Q.put((-d[G[start_ind[u] + i][1]],G[start_ind[u] + i][1]))
            processed[u] = True

    return parents, d[t]

def get_result(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y]) + [y]

def tourist_guide(G,a,b,K):
    n = len(G)
    for i in range(n): #krawędzie w drugą stronę
        G.append((G[i][1],G[i][0],G[i][2]))

    parents, d = dijkstra(G,a,b)

    if d is None:
        return False
    else:
        return get_result(parents,a,b), ceil(K/d)



graph = [(0, 1, 2), (0, 2, 4), (1, 2, 10), (1, 3, 7), (2, 4, 3), (3, 5, 1), (4, 3, 2), (4, 5, 5)]
A = 0
B = 5
K = 4
print(tourist_guide(graph,A,B,K)) #([0, 2, 4, 5], 2) (ścieżka, ilość grup)

graph = [(0, 1, 2), (0, 2, 4), (1, 2, 10), (1, 3, 7), (2, 4, 3), (3, 5, 1), (4, 3, 2), (4, 5, 5)]
A = 2
B = 3
K = 7
print(tourist_guide(graph,A,B,K)) #([2, 1, 3], 1)


graph = [(0, 1, 2), (0, 2, 4), (1, 2, 10), (1, 3, 7), (2, 4, 3), (3, 5, 1), (4, 3, 2), (4, 5, 5)]
A = 0
B = 5
K = 3
print(tourist_guide(graph,A,B,K)) #([0, 2, 4, 5], 1)

