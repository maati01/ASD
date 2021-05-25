from queue import PriorityQueue
from math import inf
import time
from random import randint
#dijsktra O(V^2)

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
                if G[v][i] != 0 and d[i] > d[v] + G[v][i]: #relaksacja
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)


    return d


'''G = [[0, 4, 0, 0, 0, 0, 0, 8, 0], #[0, 4, 12, 19, 21, 11, 9, 8, 14]
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]'''
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
'''#G = [[0, 2, 4, 0, 0, 0],
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