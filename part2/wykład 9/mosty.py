from math import inf

def low(tab_low,u,i,entry,parents): #tajemnicza funkcja low z wykładu
    if entry[u] < entry[i]:
        return entry

    tab_low[u] = entry[i]

    if tab_low[u] < entry[parents[u]]: #uzupelniam wartosci od wierzchołka u do i
        temp = parents[u]
        while temp != i:
            entry[temp] = entry[u]
            temp = parents[temp]

    return tab_low

def DFS(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    parents = [inf]*n
    entry = [0]*n #czas wejscia
    tab_low = [0]*n #czas low
    time = 0

    def dfs_visit(u):
        nonlocal G, visited,time,entry,tab_low
        time += 1
        visited[u] = True
        entry[u] = time
        tab_low[u] = time
        for i in range(n):
            if not visited[i] and G[u][i] == 1:
                parents[i] = u
                dfs_visit(i)
            elif G[u][i] == 1 and visited[i] and parents[u] != i and u > i: #krawedzie wsteczne
                tab_low = low(tab_low,u,i,entry,parents)


        time += 1

    for v in range(n): #zaczynam z kazdego wierzcholka
        if not visited[v]:
            dfs_visit(v)


    return parents,entry,tab_low

def mosty(G):
    n = len(G)
    result = []
    parents, entry,tab_low = DFS(G)
    for i in range(n):
        if parents[i] != inf and entry[i] == tab_low[i]:
            result.append((i,parents[i]))


    return result


G = [[0,1,0,0,0,0,1,0], #[(3, 2), (7, 6)]
     [1,0,1,0,0,0,0,0],
     [0,1,0,1,0,0,1,0],
     [0,0,1,0,1,1,0,0],
     [0,0,0,1,0,1,0,0],
     [0,0,0,1,1,0,0,0],
     [1,0,1,0,0,0,0,1],
     [0,0,0,0,0,0,1,0]]
G = [[0,1,0,0,0,0], #[(1, 0), (4, 3), (5, 4)]
     [1,0,1,1,0,0],
     [0,1,0,1,0,0],
     [0,1,1,0,1,0],
     [0,0,0,1,0,1],
     [0,0,0,0,1,0]]

print(mosty(G))