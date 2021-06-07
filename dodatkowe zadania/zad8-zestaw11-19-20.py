#Zadanie 8. (rozłączne ścieżki) Dany jest graf skierowany G = (V, E) oraz wierzchołki s i t. Proszę
#zaproponować algorytm znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.
import copy
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
            if not visited[i] and G[u][i] > 0:
                visited[i] = True
                d[i] = d[u] + 1
                #G[u][i] = 0 #blokuje poprzednią scieżkę
                parents[i] = u
                Q.append(i)
                if i == t:
                    return True,parents

    return False,parents

def edmonds_karp(G,s,t):
    n = len(G)
    path = True
    max_flow = 0
    flag = 1
    temp = copy.deepcopy(G)

    while(path):
        path, parents = BFS(G,s,t)

        if flag:
            G = copy.deepcopy(temp)
            flag = 0

        if path:
            temp_max = inf
            i = t
            while i != s:
                temp_max = min(temp_max,G[parents[i]][i]) #szukam "najwęższej krawędzi" w znalezionej ścieżce
                G[parents[i]][i] = 0 #usuwam sciezke w grafie
                if i != t:
                    for j in range(n):
                        G[parents[i]][j] = 0  # blokuje wszystkie krawedzie wychdozace z wierzchołków na tej ścieżce
                i = parents[i]
            max_flow += temp_max #maksymalizuje przepływ

            i = t
            while i != s: #po znalezionej ścieżce odejmuje maksymalny przepływ w stronę skierowaną(możliwy przepływ do wykorzystania)
                G[parents[i]][i] -= temp_max
                G[i][parents[i]] += temp_max #w drugą stronę dodaje ten przepływ, tyle można wyprowadzić
                i = parents[i]

    return max_flow


# 1
graph = [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]

print(edmonds_karp(graph, 0, 6))

# 2
graph = [[0, 1, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0]]

print(edmonds_karp(graph, 0, 5))