#dla BFS i DFS
#dla list sasiedztwa O(V + E)
#dla macierzy sasiedztwa O(V^2)
#

def DFS(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    entry = [0]*n #czas wejscia
    process = [0]*n #czas przetworzenia
    time = 0

    def dfs_visit(u):
        nonlocal G, visited,time
        time += 1
        visited[u] = True
        entry[u] = time
        for v in G[u]: #jesli jest implementacja macierzowa trzeba zmienic petle
            if not visited[v]: #v - 1 gdy indeksuje od 0, lub v gdy od 1
                parents[v] = u #zalezy od indeksowania u + 1, lub u
                dfs_visit(v)
        time += 1
        process[u] = time

    for v in range(n): #zaczynam z kazdego wierzcholka
        if not visited[v]:
            dfs_visit(v)


    return visited,parents,entry,process

#G = [[2,3,4],[4],[5],[6,7],[4,7],[8],[8],[]] #dla kazdego wierzchołka przechowuje liste wierzchołków do której wchodzą

#G = [["b","c"],["e","a"],["d","f","a"],["e","c"],["e","c","g"],["f","h"],["g"]]
#G = [[2,3],[1,5],[1,4,6],[3,5],[2,4,6],[3,5,7],[6,8],[8]]
#F = [[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[7]]
G = [[1,4],[2,3],[0,7],[4,6],[5],[6],[5],[9],[7,6],[10],[8,5]]
print(DFS(G))
