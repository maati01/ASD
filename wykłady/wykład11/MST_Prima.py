from queue import PriorityQueue
from math import inf

#ElogV
#drzewo w strukturze parentów

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


def mst_prima(G,v): #z wikipiedii
    n = len(G)
    parents = [None]*n
    weight = [inf]*n #waga drzewa
    weight[v] = 0
    Q = PriorityQueue()
    Q.put((weight[v],v)) #krotka trzyma akutalną wage i indeks
    vertices = [Node(i) for i in range(n)] #zbiór dla kazdego wierzchołka
    S = Node(vertices[v])

    while not Q.empty():
        temp = Q.get() #priority queue posortowane po wagach
        t = temp[1]
        S_temp = vertices[t]
        union(S,S_temp)
        y = find(vertices[t])
        #mozna dodac processed dla usprawnienia

        for u in range(n):
            x = find(vertices[u]) #sprawdzam czy x juz jest w zbiorze
            if G[t][u] != 0 and G[t][u] < weight[u] and x != y:
                weight[u] = G[t][u]
                parents[u] = t
                Q.put((weight[u],u))



    return parents

G = [[0,1,12,0,0,0],
     [1,0,7,5,0,0],
     [12,1,0,6,8,0],
     [0,5,6,0,4,3000],
     [0,0,8,4,0,9],
     [0,0,0,3000,9,0]]

print(mst_prima(G,0))