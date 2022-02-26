import math

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

    max_cost = -math.inf
    for e in result:
        if max_cost < e[2]:
            max_cost = e[2]

    return max_cost

def distance(x,y): #dystans miedzy osadami
    return math.sqrt(pow(y[0] - x[0],2) + pow(y[1] - x[1],2))

def network(coords,T):
    n = len(coords)
    k = len(T)
    graph = [[None]*n for _ in range(n)]
    edges = []

    for i in range(n): #tworzenie grafu
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = math.ceil(distance(coords[i],coords[j])) #ceil poniewaz, musimy zagwarantować że zasieg bedzie wystraczający

    for i in range(k): #tworzenie grafu
        for j in range(k):
            graph[T[i]][T[j]] = 0

    for i in range(n): #przerobienie grafu do reprezantacji krawedziowej, aby móc wywołac algorytm kruskala
        for j in range(n):
            if i != j:
                edges.append((i,j,graph[i][j]))

    return mst_kruskala(edges)

#1
coords = [(1,1),(2,1),(3,1),(4,1),
          (1,2),(2,2),(3,2),(4,2),
          (1,3),(2,3),(3,3),(4,3),
          (1,4),(2,4),(3,4),(4,4)]
T = [5,10]
print(network(coords,T))

# 5
coords = [(0, 1), (1, 3), (4, 2), (6, 6), (0, 5), (7, 5)]
T = []
print(network(coords, T))

# 4
coords = [(0, 1), (1, 3), (4, 2), (6, 6), (0, 5), (7, 5)]
T = [5, 3, 2]
print(network(coords, T))