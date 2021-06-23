from collections import deque
from math import inf
#poprawiony algorytm Forda Fulkersona
#Algorytm Edmondsa-Karpa jest jedną z realizacji metody Forda-Fulkersona rozwiązywania problemu maksymalnego przepływu w sieci przepływowej
#O(V*E^2)

def BFS(G,s,t): #indeksuje grafy od zera, lekko zmodyfikowany BFS
    n = len(G)
    Q = deque()
    visited = [False]*n
    d = [-1]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.append(s)
    visited[s] = True

    while Q:
        u = Q.popleft()
        for i in range(n):
            if not visited[i] and G[u][i] != 0:
                visited[i] = True
                d[i] = d[u] + 1
                parents[i] = u
                Q.append(i)
                if i == t:
                    return True,parents

    return False,parents

def edmonds_karp(G,s,t):
    path = True
    max_flow = 0

    while(path):
        path, parents = BFS(G,s,t)

        if path:
            temp_max = inf
            i = t
            while i != s:
                temp_max = min(temp_max,G[parents[i]][i]) #szukam "najwęższej krawędzi" w znalezionej ścieżce
                i = parents[i]

            max_flow += temp_max #maksymalizuje przepływ

            i = t
            while i != s: #po znalezionej ścieżce odejmuje maksymalny przepływ w stronę skierowaną(możliwy przepływ do wykorzystania)
                G[parents[i]][i] -= temp_max
                G[i][parents[i]] += temp_max #w drugą stronę dodaje ten przepływ, tyle można wyprowadzić
                i = parents[i]

    return max_flow


# 23
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

#print(edmonds_karp(graph, 0, 5))

# 5
graph = [[0, 8, 3, 0, 0, 0],
         [0, 0, 0, 9, 0, 0],
         [0, 0, 0, 7, 4, 0],
         [0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0]]

#print(edmonds_karp(graph, 0, 5))

# 19
graph = [[0, 10, 10, 0, 0, 0],
         [0, 0, 2, 4, 8, 0],
         [0, 0, 0, 0, 9, 0],
         [0, 0, 0, 0, 0, 10],
         [0, 0, 0, 6, 0, 10],
         [0, 0, 0, 0, 0, 0]]
#print(edmonds_karp(graph, 0, 5))
#19
graph = [[0,10,0,0,0,10],
         [0,0,4,0,8,2],
         [0,0,0,10,0,0],
         [0,0,0,0,0,0],
         [0,0,6,10,0,0],
         [0,0,0,0,9,0]]

#print(edmonds_karp(graph, 0, 3))