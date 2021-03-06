from queue import PriorityQueue
from math import inf
import time
from random import randint

class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0 #oszacowanie wysokości drzewa, nie bedzie dokladne
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x,y):
    x = find(x) #szukam reprezentanta zbioru
    y = find(y)

    if x == y: return #sytacja gdy sa w tym samym zbiorze

    if x.rank > y.rank: #"przyklejam" y do x, wysokość drzewa nie wzrosłą
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: #potencjalnie drzewo mogło urosnąć
            y.rank += 1

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
    vertices = [Node(i) for i in range(n)]  # zbiór dla kazdego wierzchołka
    S = Node(vertices[v])

    while not Q.empty():
        temp = Q.get() #priority queue posortowane po oszacowanych dystansach
        u = temp[1]
        distance[u] = temp[0]
        S_temp = vertices[u]
        union(S,S_temp)
        x = find(S) #gorsza zlozonosc


        if not processed[u]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                y = find(vertices[i])
                if G[u][i] != 0 and d[i] > d[u] + G[u][i] and x != y: #relaksacja
                    d[i] = d[u] + G[u][i]
                    parents[i] = u
                    distance[i] = d[i]
                    Q.put((distance[i],i))
            processed[u] = True


    return d

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0], #[0, 4, 12, 19, 21, 11, 9, 8, 14]
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
# [0, 2, 3, 8, 6, 9]
'''G = [[0, 2, 4, 0, 0, 0],
         [0, 0, 1, 7, 0, 0],
         [0, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 2, 0, 5],
         [0, 0, 0, 0, 0, 0]]'''

# [0, 4, 4, 2, 1, 4]
'''G = [[0, 5, 4, 2, 1, 6],
         [1, 0, 6, 3, 4, 2],
         [2, 9, 0, 4, 3, 5],
         [9, 2, 7, 0, 6, 2],
         [8, 6, 4, 7, 0, 8],
         [2, 1, 3, 7, 3, 0]]'''
'''G = [[0, 2, 4, 0, 0, 0],
         [0, 0, 1, 7, 0, 0],
         [0, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 2, 0, 5],
         [0, 0, 0, 0, 0, 0]]'''

n = 3000
rr = (1, n)
G = [[0 if i == j else randint(rr[0], rr[1]) for i in range(n)] for j in range(n)]

start_time = time.time()
dijkstra(G,0)
print("--- %s seconds ---" % (time.time() - start_time))