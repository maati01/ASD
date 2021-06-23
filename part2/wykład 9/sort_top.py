#działa dla sortowania dagów (directed acyclic graph)

def DFS(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    tab = [] #lista ktora trzyma kolejnosc

    def dfs_visit(u):
        nonlocal G, visited,tab
        visited[u] = True
        for v in G[u]:
            if not visited[v]: #v - 1 gdy indeksuje od 0, lub v gdy od 1
                parents[v] = u #zalezy od indeksowania u + 1, lub u
                dfs_visit(v)
            #if not v in tab:  # gdy dojde na koniec wrzucam do tablicy/na dół stosu
                tab.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)
            tab.append(v) #wierzchołek idzie na początek/góre stosu

    return tab[::-1]

#G = [[1,2],[2,4],[],[],[3,5,6],[],[],[4],[7]]
#G = [[1,2],[2,4],[],[],[3,5,6],[],[]]
#G = [[1],[],[]]
#G = [[1],[2],[3],[4],[5],[]]
#G = [[1,5],[2],[3],[4],[5],[]]
G = [[1,5],[2],[3,0,1,2],[4],[5],[],[3]]
print(DFS(G))