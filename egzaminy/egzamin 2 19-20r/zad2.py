from zad2testy import runtests
from math import ceil
from math import sqrt
from math import inf

#tworze wszystkie mozliwe autostrady
#dla kazdej odpalam kruskala
#szukam min roznice czasu
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

def mst_kruskala(G,edge):
    n = len(G)
    cnt = 0
    G = sorted(G, key = lambda x: x[2]) #sortowanie po wagach
    result = []
    vertices = [0]*(2*n + 1) #wierzchołki jakie występują,potencajalnie

    vertices[edge[0]] = 1
    vertices[edge[1]] = 1
    for i in range(1,n): #1 jesli wystepuje wierzchołek
        if G[i] != edge:
            vertices[G[i][0]] = 1
            vertices[G[i][1]] = 1

    for j in range(n): #liczba wierzchołków
        if vertices[j] == 1:
            cnt += 1

    vertices = [Node(i) for i in range(cnt + 1)] #zbiór dla kazdego wierzchołka


    i = 0
    e = 0 #indeks dla ilosci krawędzi
    flag = False

    while e < cnt and i < n:
        if flag and G[i] != edge:
            u, v, w = G[i]
        else:
            u, v, w = edge
            flag = True
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

    return result

def highway(A):
    n = len(A)
    edges = []

    for i in range(n):
        for j in range(i + 1,n):
            edges.append((i,j,ceil(sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2))))

    n = len(edges)

    min_diff = inf
    for i in range(n):
        result = mst_kruskala(edges,edges[i])

        temp_min = inf
        temp_max = -inf
        for j in range(len(result)):
            if temp_min > result[j][2]:
                temp_min = result[j][2]

            if temp_max < result[j][2]:
                temp_max = result[j][2]

        if temp_max - temp_min < min_diff:
            min_diff = temp_max - temp_min

    return min_diff

runtests( highway )