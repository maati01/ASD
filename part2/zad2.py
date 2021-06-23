from zad2testy import runtests
from collections import deque
#Mateusz Powęska

#wywołuje bfs i szukam najkrótszej ścieżki
#wywołuje bfsa drugi raz dla kazdego wierzchołka poza startowym i szukam czy jest dluzsza sciezka, jesli tak to mozna usunac, jesli nie to None
def BFS(G, s): #indeksuje grafy od zeram typowy bfs z wykładu
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
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parents[v] = u
                Q.append(v)

    return d

def enlarge(G, s,t):
    d = BFS(G,s)
    min = d[t]


    for v in G[s]: #przeszukuje sciezki poza startowym i sprawdzam czy jest mozliwe uzyskac innej sciezki, wiekszej
        d2 = BFS(G,v)
        if min > d2[t]:
            return (s,v)



    return None

runtests( enlarge ) 
