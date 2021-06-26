from zad3testy import runtests
from queue import PriorityQueue
from math import inf

#dijsktra O(V^2)
#zmydofikowana dijkstra, 'rozbijam' kazdy wierzchołek na 3, gdzie:
#1 - moze uzyc butów
#2 - właśnie używa butów
#3 - nie może użyc butów

def dijkstra(G,old_G,v): #z wikipiedii
    n = len(G)
    d = [[inf,inf] for _ in range(n)]
    parents = [None]*n
    processed = [[False,False] for _ in range(n)] #wierzchołki przetworzone
    d[v] = [0,0]
    flag = True #flaga, true jesli moze uzyc butów
    Q = PriorityQueue()
    Q.put((d[v],v,flag)) #krotka trzyma akutalny dystans i indeks
    while not Q.empty():
        temp = Q.get() #priority queue posortowane po oszacowanych dystansach
        u = temp[1]
        d[u] = temp[0]
        flag = temp[2]
        if not processed[u][0] or not processed[u][1]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[u][i] != 0 and d[i][0] > d[u][0] + G[u][i] and flag and old_G[u][i] != 0:  # nie uzylem butów i nadal ich nie uzywam
                    d[i][0] = d[u][0] + old_G[u][i]
                    parents[i] = u
                    Q.put((d[i], i, True))
                if G[u][i] != 0 and d[i][1] > d[u][0] + G[u][i] and flag and (old_G[u][i] > G[u][i] or old_G[u][i] == 0):  # nie uzyłem butów ale teraz ich uzywam
                    d[i][1] = d[u][0] + G[u][i]
                    parents[i] = u
                    Q.put((d[i], i, False))
                if G[u][i] != 0 and d[i][0] > d[u][1] + G[u][i] and not flag and old_G[u][i] != 0:  # użyłem butów i teraz ich nie używam
                    d[i][0] = d[u][1] + old_G[u][i]
                    parents[i] = u
                    Q.put((d[i], i, True))


            if flag: #warunek przetworzenia w dwóch sytacjach, gdy uzylem i nie uzylem butów
                processed[u][0] = True
            else:
                processed[u][1] = True

    return d

def new_edges(G): #funkcja tworzy nowe krawędzie z zasadami dwumilowych butów, tworzac nowy graf
    n = len(G)
    new_G = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_G[i][j] = G[i][j]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G[i][j] != 0 and G[j][k] != 0 and i != k:
                    if new_G[i][k] != 0:
                        temp = new_G[i][k]
                        new_G[i][k] = min(max(G[i][j],G[j][k]),temp) #minimalizyje po mozliwych krawedziach
                    else:
                        new_G[i][k] = max(G[i][j], G[j][k])
    print(new_G)

    return new_G

def jumper(G, s, w):
    new_G = new_edges(G)
    d = dijkstra(new_G,G,s)
    return min(d[w])


runtests(jumper)

