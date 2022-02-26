from zad3testy import runtests

#zwykły topo sort
#trzeba tylko odpowiedno skierowac krawedzie zgodnie z poleceniem
#dla macierzowej O(V^2)

def DFS(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    tab = [] #lista ktora trzyma kolejnosc

    def dfs_visit(u):
        nonlocal G, visited,tab
        visited[u] = True
        for v in range(len(G[u])):
            if not visited[v] and G[u][v] != 0:
                parents[v] = u
                dfs_visit(v)
                tab.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)
            tab.append(v)

    return tab[::-1]

def tasks(T):
    n = len(T)

    for i in range(n):
        for j in range(n): #kieruje odpowiednio krwedz b -> a
            if T[i][j] == 2:
                T[i][j] = 0
                T[j][i] = 1

    return DFS(T)

runtests( tasks )