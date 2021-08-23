#sortuje topologicznie
#jeśli wierzchołki po sortowaniu topologicznym mają między nastepnymi krawedzie to znaczy ze mamy sciezke hamiltona
#gwarantuje nam to kolejność przetowrzenia wierzchołków
#w przeciwynym wypadku nie ma sciezki hamiltona
#O(V + E)
def top_sort(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
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


def hamilton_path(G):
    tab = top_sort(G)
    n = len(tab)


    for i in range(n-1):
        flag = False
        for j in range(len(G[tab[i]])):
            if G[tab[i]][j] == tab[i+1]:
                flag = True
        if not flag:
            return False

    return True





G = [[1],[2,4],[3],[4],[5],[]] #True
print(hamilton_path(G))
G = [[1],[2,6],[3],[4],[5],[],[]] #False
print(hamilton_path(G))
G = [[1],[5,4],[],[4],[2],[3]] #True
print(hamilton_path(G))
G = [[1],[2,4],[],[4],[5],[]] #False
print(hamilton_path(G))