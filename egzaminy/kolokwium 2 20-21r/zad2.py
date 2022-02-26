from zad2testy import runtests
from queue import Queue
from math import inf


# puszczam dwa bfsy
# od s, zapisuje dystans, rodzciów oraz czy są odwiedzone
# od t, jeśli napotkam wierzchołek v, do którego doszedłem z wierzchołka s
# oraz odległość od t do v plus v do s jest większa od odległości s do t
# to oznacza, że znalazłem dłuższą ścieżkę a krawędź między u oraz jego dzieckiem może zostać usunięta
# krawędź została zapisana przy pierwszym użyciu bfsa, który znalazł najkrótszą ścieżkę
# O(V + E)

def BFS(G, s):
    n = len(G)
    Q = Queue()
    d = [inf] * n
    visited = [False] * n
    visited[s] = True
    parents = [None] * n
    d[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parents[v] = u
                Q.put(v)

    return visited, parents, d


def modified_BFS(G, s, visited, last_d):
    n = len(G)
    Q = Queue()
    d = [-1] * n
    new_visited = [False] * n
    new_visited[s] = True
    d[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not new_visited[v]:
                if visited[v] and d[u] + last_d[v] + 1 > last_d[s]:
                    return u

                new_visited[v] = True
                Q.put(v)

    return None


def enlarge(G, s, t):
    visited, parents, d = BFS(G, s)

    if d[t] == inf:
        return None

    v = modified_BFS(G, t, visited, d)

    if v is None:
        return None
    else:
        if parents[v] is None:
            return (s, v)
        else:
            return (parents[v], v)


runtests(enlarge)
