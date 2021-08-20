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
        for v in range(len(G[u])):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                d[v] = d[u] + 1
                parents[v] = u
                Q.put(v)

    return parents