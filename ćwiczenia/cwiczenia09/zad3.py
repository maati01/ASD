#zwykły bfs
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

    return d

G = [[1],[2,4],[3],[4],[5],[]] #[0, 1, 2, 3, 2, 3]
print(BFS(G,0))
G = [[1],[2,6],[3],[4],[5],[],[]] #[0, 1, 2, 3, 2, 3]
print(BFS(G,0))
G = [[1],[2,4],[3],[4],[5],[]] #[-1, -1, 0, 1, 2, 3]
print(BFS(G,2))