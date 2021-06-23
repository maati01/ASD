from queue import Queue


def BFS(G, s): #indeksuje grafy od zera
    n = len(G)
    Q = Queue()
    visited = [False]*n
    d = [-1]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]: #v i v - 1/ u i u - 1 w zaleznosci od indeksowania
                visited[v] = True
                d[v] = d[u] + 1
                parents[v] = u
                Q.put(v)

    return visited,d,parents

G = [[2,3,4],[4],[5],[6,7],[4,7],[8],[8],[]] #dla kazdego wierzchołka przechowuje liste wierzchołków do której wchodzą
print(BFS(G,0))