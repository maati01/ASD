from collections import deque


def czy_dwudzielny(G): #indeksuje grafy od zera
    s = 0
    n = len(G)
    Q = deque()
    visited = [False]*n
    tab = [-1]*n #tablica do sprawdzania dwudzilnosci
    Q.append(s)
    visited[s] = True
    tab[s] = 0

    while Q:
        u = Q.popleft()
        curr = tab[u]
        for v in G[u]:
            if visited[v] and tab[v] == curr: #gdy dwie sasiadujace wierzcholki maja taka sama wartość graf nie jest dwudzielny
                return False

            elif not visited[v]: #v i v - 1/ u i u - 1 w zaleznosci od indeksowania
                visited[v] = True
                tab[v] = 1 - curr #ustawiam na drugą wartość
                Q.append(v)


    return True

#G = [[4,5,6],[4,5,6],[4,5,6],[1,2,3],[1,2,3],[1,2,3]]
G =  [[3, 5],[2, 6],[1],[0, 4],[3],[0, 6],[1, 5]]
#G = [[3, 5],[2, 6],[1],[0, 4, 5],[3],[0, 3, 6],[1, 5]]
#G = [[],[],[]]

print(czy_dwudzielny(G))

