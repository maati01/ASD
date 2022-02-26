#sortuje krawedzie
#sprawdzam dla wszystkich róznych krawedzi czy da się przelecieć na pułapie min_edge + t
#jesli nie sprawdzam nastepna krawedz


def DFS(G,x,val,t): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    parents = [None]*n

    def dfs_visit(u):
        visited[u] = True
        for v in range(len(G[u])):
            if not visited[v] and G[u][v] != 0 and abs(G[u][v] - val) <= t:
                parents[v] = u
                dfs_visit(v)
    dfs_visit(x)
    return parents

def get_solution(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_solution(parents,x,parents[y]) + [y]

def best_fly(G,x,y,t):
    edges = []
    n = len(G)
    for i in range(n):
        for j in range(i,n):
            if G[i][j] != 0:
                edges.append(G[i][j])

    edges.sort()

    prev = -1
    parents = None
    for i in range(len(edges)):
        if edges[i] != prev:
            parents = DFS(G,x,edges[i] + t,t)
            prev = edges[i]
        if parents[y] is not None:
            return get_solution(parents,x,y), edges[i] + t

    return False




G = [[0,4,5,6,0,0,0,0],
     [4,0,0,0,0,0,9,0],
     [5,0,0,0,0,8,0,0],
     [6,0,0,0,0,0,0,4],
     [0,0,0,0,0,9,7,5],
     [0,0,8,0,9,0,10,0],
     [0,9,0,0,7,10,0,0],
     [0,0,0,4,5,0,0,0]]
print(best_fly(G,0,6,2)) #([0, 3, 7, 4, 6], 6) (ścieżka, pułap)

G = [[0,4,5,6,0,0,0,0],
     [4,0,0,0,0,0,9,0],
     [5,0,0,0,0,8,0,0],
     [6,0,0,0,0,0,0,4],
     [0,0,0,0,0,9,9,5],
     [0,0,8,0,9,0,10,0],
     [0,9,0,0,9,10,0,0],
     [0,0,0,4,5,0,0,0]]
print(best_fly(G,0,6,2)) #([0, 2, 5, 4, 6], 7)

G = [[0,4,5,6,0,0,0,0],
     [4,0,0,0,0,0,9,0],
     [5,0,0,0,0,8,0,0],
     [6,0,0,0,0,0,0,4],
     [0,0,0,0,0,9,11,5],
     [0,0,8,0,9,0,10,0],
     [0,9,0,0,11,10,0,0],
     [0,0,0,4,5,0,0,0]]
print(best_fly(G,0,6,2)) #False