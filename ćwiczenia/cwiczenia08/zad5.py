#minimalizuje liczbe opłat do danego wierzchołka
#pole visited ustawiam na true tylko wtedy gdy sprawdze wszytkie grawedzie z niego wychodzace
#to pogarsza zlozonosc wzgledem zwyklego bfsa
#brzmi troche jak dynamiczne
#O(v^3), można lepiej

from queue import Queue
from math import inf

def BFS(G, s): #zmodyfikowany BFS
    n = len(G)
    Q = Queue()
    visited = [False]*n
    amount_of_fees = [inf]*n
    amount_of_fees[s] = 0
    parents = [None]*n
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(len(G[u])):
            if G[u][v] != 0 and not visited[v]:
                if G[u][v] == 'P' and amount_of_fees[u] + 1 < amount_of_fees[v]:
                    amount_of_fees[v] = amount_of_fees[u] + 1
                    parents[v] = u
                    if Q.empty() or v not in Q.queue: #przez to O(v^3)
                        Q.put(v)
                elif G[u][v] != 'P' and amount_of_fees[u] < amount_of_fees[v]:
                    amount_of_fees[v] = amount_of_fees[u]
                    parents[v] = u
                    if Q.empty() or v not in Q.queue:
                        Q.put(v)
            G[u][v] = 0

    return parents

def get_result(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y]) + [y]

def min_fees(G,x,y):
    parents = BFS(G, x)

    if parents[y] is None:
        return False
    else:
        return get_result(parents,x,y)

#P - paid
#[0, 6, 5, 3]
G = [[0,1,0,0,'P',0,1],
     [1,0,'P',0,0,0,0],
     [0,'P',0,'P',0,0,0],
     [0,0,'P',0,'P',1,0],
     ['P',0,0,'P',0,0,0],
     [0,0,0,1,0,0,'P'],
     [1,0,0,0,0,'P',0]]
print(min_fees(G,0,3))

# [0, 2, 4, 3]
graph = [[0, 'P', 1, 0, 0],
         [0, 0, 0, 'P', 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0]]
print(min_fees(graph,0,3))

# [0, 2, 3, 1]
graph = [[0, 'P', 1, 0],
         ['P', 0, 0, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]]
print(min_fees(graph,0,1))

