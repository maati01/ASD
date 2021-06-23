from collections import deque
from math import inf

#uproszczenie:
#uniemożliwić komunikację z A do B(nie z B do A).Linie telegraficzne są skierowane.

#min_cut = max_flow

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

def BFS_classic(G, s): #indeksuje grafy od zera
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

    return visited

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


    return G

def subversion(cities,lines,A,B):
    S = [] #zbiory na wierzchołki
    T = []
    n = len(lines)
    k = len(cities)

    G = [[0]*k for _ in range(k)]

    for i in range(n):
        G[lines[i][0]][lines[i][1]] = lines[i][2]


    G = edmonds_karp(G,A,B) #G to siec residualna

    visited = BFS_classic(G,A)

    for i in range(k): #generowanie zbiorów
        if visited[i]:
            S.append(i)


    for i in range(k):
        if not visited[i]:
            T.append(i)

    x = len(S)
    y = len(T)
    min_val = 0
    result = []


    for i in range(x): #szukanie krawędzi miedzy zbiorami S oraz T w sieci residualnej, ich suma to max_flow (min_cut)
        for j in range(y):
            if G[S[i]][T[j]] != 0:
                min_val += G[S[i]][T[j]]
                result.append((T[j],S[i],G[S[i]][T[j]]))
            elif G[T[j]][S[i]]:
                min_val += G[T[j]][S[i]]
                result.append((S[i],T[j], G[T[j]][S[i]]))
    return min_val,result


#(5, [(2, 1, 3), (4, 1, 2)])
cities = [0, 1, 2, 3, 4] #dla uproszczenia daje indeksy samiast stringów, mozna zmapować dla w razie potrzeb
lines = [[0, 3, 3],
        [0, 2, 4],
        [3, 4, 3],
        [2, 4, 2],
        [2, 1, 3],
        [4, 1, 2]]

print(subversion(cities,lines,0,1))

#(3, [(0, 2, 1), (1, 2, 1), (3, 2, 1)])
cities = [0,1,2,3]
lines = [[0,1,2],
         [0,3,2],
         [0,2,1],
         [3,2,1],
         [1,2,1]]
print(subversion(cities,lines,0,2))

#(3, [(0, 2, 1), (1, 2, 1), (3, 2, 1)])
cities = [0,1,2,3,4]
lines = [[0,1,2],
         [0,3,2],
         [0,2,1],
         [3,2,1],
         [1,2,1],
         [2,4,4]]
print(subversion(cities,lines,0,4))

#(2, [(2, 4, 2)])
cities = [0,1,2,3,4]
lines = [[0,1,2],
         [0,3,2],
         [0,2,1],
         [3,2,1],
         [1,2,1],
         [2,4,2]]
print(subversion(cities,lines,0,4))
