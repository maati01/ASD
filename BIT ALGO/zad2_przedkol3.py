from collections import deque
from math import inf

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

    return max_flow,G

def internet_cafe(A,T,K):
    n = len(A)
    graph = [[0]*(n + K + 2) for _ in range(n + K + 2)]

    for i in range(n): #pierwszy dodatkowy wierzchołek - źródło, na krawędziach liczba potrzebnych aplikacji
        graph[0][i + 1] = T[i] #skierowany


    for i in range(K): #drugi dodadtkowu wierzchołek - ujście
        graph[n + i + 1][n + K + 1] = 1


    for i in range(n): #tworze graf
        for v in A[i]:
            graph[i + 1][v + n + 1] = 1

    res,G = edmonds_karp(graph,0,n + K + 1)

    if res < sum(T):
        return False

    else:
        result = [0]*K
        k = 0
        for i in range(n + 1,n + K + 1): #aplikacje do komputerów
            for j in range(n + K + 2):
                if G[i][j] == 1:
                    result[k] = j - 1
                    k += 1
        return True,result



#True
K = 4
A = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0]]  # aplikacje
T = [0,1,2,1,0,0] #ilosc aplikacji których potrzebujemy
print(internet_cafe(A,T,K))

#True
K = 4
A = [[0, 1], [0,3], [0, 1, 2, 3], [3], [1,3], [0]]  # aplikacje
T = [0,1,2,1,0,0] #ilosc aplikacji których potrzebujemy
print(internet_cafe(A,T,K))

#True
K = 6
A = [[0, 1], [0,3], [0, 1, 2, 3], [3], [1,3], [0,4,5]]
T = [0,1,2,1,0,2]
print(internet_cafe(A,T,K))

#False
K = 6
A = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0,4,5]]
T = [0,1,2,1,0,2]
print(internet_cafe(A,T,K))

#False
Z = [2, 1, 1] # Z[i] zapotrzebowanie na ita aplikacje
K = 4 # ilosc komputerow
A = 3 # ilosc aplikacji
C = [[0], [2, 1], [3]] # lista kompatybilnosci aplikacji z komputerami
print(internet_cafe(C,Z,K))

#False
K = 4
A = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0]]  # aplikacje
T = [0,1,2,1,0,1] #ilosc aplikacji których potrzebujemy
print(internet_cafe(A,T,K))