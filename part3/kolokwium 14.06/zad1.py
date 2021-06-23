from zad1testy import runtests
from math import inf
from collections import deque

#Mateusz Powęska
#uruchamiam algorytm floyda warshalla
#sprawdzam gdzie odleglosci sciezek sa zgodne z warunkiem zadania >= d
#tworze na tej podstawie graf
#szukam w tym zmodyfikowanym grafie sciezki
#wracam po sciezce w wyjsciowym grafie i sprawdzam czy zgadza sie z grafem wygenerowanym przez floyda warshalla
#dzieki temu wiem gdzie w danym momencie sa dwie postacie w odległosci >= d, którą gwarantuje mi nowo wygenerowana macierz

def BFS(G, s): #indeksuje grafy od zera
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
            if not visited[i] and G[u][i] != 0: #v i v - 1/ u i u - 1 w zaleznosci od indeksowania grafu
                visited[i] = True
                d[i] = d[u] + 1
                parents[i] = u
                Q.append(i)

    return d,parents

def floyd_warshall(G):
    n = len(G)

    P = [[None]*n for _ in range(n)] #poprzednik v na najkrótszej ścieżce z u do v,parents
    S = [[inf]*n for _ in range(n)] #macierz dł. najkrótszych ścieżek używających {v1,...,vt} jako wewnętrzne

    for i in range(n):
        S[i][i] = 0

    for i in range(n): #bezposrednie krawedzie jako minimalne sciezki wyjsciowe
        for j in range(n):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
                P[i][j] = i

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]

    return S

def keep_distance(M, x, y, d):
    n = len(M)
    S = floyd_warshall(M)

    for i in range(n):
        for j in range(n):
            if S[i][j] >= d:
                S[i][j] = 1
            else:
                S[i][j] = 0

    while True: #moge zrobica taka petle ze wzgledu na polecenie, jest gwarancja takiej sciezki
        d,parents = BFS(M,x)
        path = []
        result = []
        temp = y


        while parents[temp] != None:
            M[temp][parents[temp]] = 0
            path.append(temp)
            temp = parents[temp]
        path.append(temp)

        for i in range(n):
            for j in range(len(path)):
                if S[i][path[j]] != 0:
                    result.append((i,path[j]))

        return result


runtests( keep_distance )