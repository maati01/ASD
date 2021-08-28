from zad1testy import runtests
from queue import Queue
from math import inf

#dwa razy BFS zeby znalezc srednice grafu
#wybieram srodkowy wierzcholek

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

def best_root( L ):
    n = len(L)

    d = BFS(L, 0)

    temp_max = -inf
    temp_ind = 0

    for i in range(n):
        if d[i] > temp_max:
            temp_ind = i
            temp_max = d[i]

    d = BFS(L, temp_ind)

    temp_max = -inf

    for i in range(n):
        if d[i] > temp_max:
            temp_max = d[i]

    for i in range(n):  # wybieram punkt który lezy pośrodku
        if d[i] == temp_max // 2 and temp_max % 2 == 0:
            return i
        elif d[i] == temp_max // 2 + 1 and temp_max % 2 != 0:
            return i


runtests( best_root )