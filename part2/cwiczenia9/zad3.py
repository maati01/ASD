from queue import Queue


def BFS(G, s): #indeksuje grafy od zera
    n = len(G)
    Q = Queue()
    visited = [False]*n
    d = [0]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if not visited[i] and G[u][i] == 1:
                visited[i] = True
                d[i] = d[u] + 1
                parents[i] = u
                Q.put(i)

    return visited,d,parents

G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]
print(BFS(G,0))