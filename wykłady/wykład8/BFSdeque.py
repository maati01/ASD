from collections import deque


def BFS(G, s): #indeksuje grafy od zera
    n = len(G)
    Q = deque()
    visited = [False]*n
    d = [-1]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.append(s)
    visited[s] = True

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v-1]: #v i v - 1/ u i u - 1 w zaleznosci od indeksowania grafu
                visited[v-1] = True
                d[v-1] = d[u] + 1
                parents[v-1] = u + 1
                Q.append(v-1)

    return visited,d,parents

G = [[2,3,4],[4],[5],[6,7],[4,7],[8],[8],[]]
print(BFS(G,0))