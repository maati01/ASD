#min spanning tree
#minimalne drzewo rozpinajace
#spojny graf nieskierwowany
#(ElogE)
#zwraca drzewo reprezentowane jako zbior krawedzi

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

def mst_kruskala(G):
    n = len(G)
    cnt = 0
    G = sorted(G, key = lambda x: x[2]) #sortowanie po wagach
    result = []
    vertices = [0]*n #wierzchołki jakie występują,potencajalnie
    for i in range(n): #1 jesli wystepuje wierzchołek
        vertices[G[i][0]] = 1
        vertices[G[i][1]] = 1

    for j in range(n): #liczba wierzchołków
        if vertices[j] == 1:
            cnt += 1

    vertices = [Node(i) for i in range(cnt)] #zbiór dla kazdego wierzchołka


    i = 0
    e = 0 #indeks dla ilosci krawędzi

    while e < cnt and i < n:
        u, v, w = G[i]
        i += 1
        x = find(vertices[u])
        y = find(vertices[v])

        if x != y: #nie zawiera cyklu
            e += 1
            result.append([u, v, w])
            union(x, y)

    min_cost = 0
    for e in result:
        min_cost += e[2]

    return result,min_cost





G = [(0,1,1),(1,2,7),(2,0,8),(2,5,3),(2,3,2),(3,4,5),(0,4,4),(0,5,12),(5,4,6)] #krotka trzymajaca krawedz miedzy dwoma wierzchołkami i wage, graf jest nieskierowany
#G = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
print(mst_kruskala(G))