from queue import PriorityQueue
from math import inf

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind


def dijkstra(G,v):
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != -1 and d[i] > d[v] + G[v][i]: #relaksacja
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)


    return d,parents

def min_cycle(G):
    min = inf
    n = len(G)
    F = [] #tablica trzyma dystanse miedzy wierzchołkiem s i v
    new_parents = []
    temp_result = []
    result = []
    temp = 0

    for i in range(n):
        d,parents = dijkstra(G,i)
        F.append(d)
        new_parents.append(parents)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    if F[i][j] != inf and F[i][k] != inf and G[j][k] != -1 and new_parents[k][i] != new_parents[j][i] and min > F[i][j] + F[i][k] + G[j][k]:
                        min = F[i][j] + F[i][k] + G[j][k]
                        temp = (i,j,k)

    if temp != 0:
        i, j, k = temp
        temp2 = k
        result.append(j)
        while j != i:
            result.append(new_parents[i][j])
            j = new_parents[i][j]
        while k != i:
            temp_result.append(new_parents[i][k])
            k = new_parents[i][k]
        ind = 0
        while temp_result[ind] != i:
            result.append(temp_result[ind])
            ind += 1
        result.append(temp2)

    return result,min


'''G = [[-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]'''

G = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]

'''G = [[-1,2,4,-1],
     [2,-1,3,-1],
     [4,3,-1,-1],
     [-1,-1,-1,-1]]'''
'''G = [[-1,-1,4,-1],
     [-1,-1,3,-1],
     [4,3,-1,-1],
     [-1,-1,-1,-1]]'''
'''G = [
[-1, 0, -1, -1],
[0, -1, 3, 2],
[-1, 3, -1, 1],
[-1, 2, 1, -1]
]'''

'''G = [
[-1, 0, -1, -1, -1],
[0, -1, 0, -1, -1],
[-1, 0, -1, 3, 2],
[-1, -1, 3, -1, 1],
[-1, -1, 2, 1, -1]
]'''


print(min_cycle(G))