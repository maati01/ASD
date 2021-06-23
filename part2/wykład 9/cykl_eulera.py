from copy import deepcopy
from collections import deque


# dla każdego wierzchołka mam maksymalnie n wywołań pętli więc złożoność obliczeniowa wynosi n^2
def BFS(G, s):  # indeksuje grafy od zera, sprawdzam spójnośc grafu
    n = len(G)
    Q = deque()
    visited = [False] * n
    Q.append(s)
    visited[s] = True

    while Q:
        u = Q.popleft()
        for i in range(n):
            if not visited[i] and G[u][i] == 1:
                visited[i] = True
                Q.append(i)

    for i in range(n):  # jesli po wywołaniu bfsa wszystkie krawedzie za odwiedzone do graf jest spójny
        if visited[i] == False:
            return False

    return True


def check(G):  # funkcja sprawdza parzystość wierzchołków
    n = len(G)
    cnt = 0
    if n < 4:
        return False

    for i in range(n):
        for j in range(n):  # zliczam ilość krawędzi
            if G[i][j] == 1:
                cnt += 1
        if cnt % 2 != 0:
            return False
        cnt = 0

    return True


def euler(G):
    if not check(G):  # sprawdzam parzystosc i ilosc wierzchołków
        return None

    if not BFS(G, 0):  # sprawdzam spójność, zlozonosc BFSa to n^2
        return None

    n = len(G)
    visited = [False for _ in range(n)]  # tablica okresla czy wierzchołek został przetworzony
    tab = []  # stos
    result = []  # tutaj tworze wynik
    last = [
               0] * n  # tablica trzyma dla kazdego wierzchołka numer wierzchołka na którym skończyła, poprawia to złożoność i zabezpiecza przed sytacja n^3
    tab.append(0)  # dodaje do stosu wierzchołek od którego zaczynam
    s = 0  # zaczynam od wierzchołka 0
    while (len(tab)):  # dopóki mam stos szukam wierzchołków do cyklu
        if visited[s] != -1:  # sprawdzam wierzchołek gdy ma jeszcze krawedzie
            for i in range(last[s], n):  # sprawdzam od ostatniego wierzchołka na którym skończyłem
                if G[s][i] == 1:  # jesli ma krawedz to ja sprawdzam
                    G[s][i] = -1  # usuwam krawedz w obie strony(-1 oznacza usuniecie krawedzi)
                    G[i][s] = -1
                    last[s] = i  # zapamietuje do którego wierzchołka sprawdziłem w danym wierzchołku
                    tab.append(i)  # dodaje wierzchołek do stosu
                    s = i  # biore wierzchołek do sprawdzenia
                    break  # przerywam fora dla danego wierzchołka i sprawdzam dla niego mozliwe przejscia
                if i == n - 1:
                    visited[s] = True  # przrobiony wierzchołek oznaczam jako true, czyli brak krawędzi
        if visited[s]:  # jeśli przerobiłem wierzchołek usuwam go ze stosu i dodaje do rezultatu
            tab.pop()
            result.append(s)
            if len(tab) != 0:  # przerbiam wierzchołek który jest na górze stosu
                s = tab[-1]

    for i in range(n):
        for j in range(n):  # przywracam macierz do stanu pierwotnego
            if G[i][j] == -1:
                G[i][j] = 1

    if result[0] == result[
        len(result) - 1]:  # jeśli wróciłem do miejsca od którego zaczynał oznacza to że mam cykl Eulera
        return result
    else:
        return None





G = [[0,1,1,0,0,0],[1,0,1,1,0,1],[1,1,0,0,1,1],[0,1,0,0,0,1],[0,0,1,0,0,1],[0,1,1,1,1,0]]
# [0, 5, 4, 1, 5, 2, 0, 4, 3, 1, 0]
#G = [[0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0]]
# [0, 4, 5, 6, 2, 5, 1, 6, 7, 3, 2, 1, 0]
#G = [[0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]
# [0, 4, 5, 3, 4, 2, 0, 3, 1, 0]
#G = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]
#G = [[0,1,0],[1,0,1],[0,1,0]]
# None
#G = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

# None
#G = [[0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0]]
#G = [[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[1,1,1,1,1,0]]
#G = []
#G = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]]
# [0, 5, 4, 1, 5, 2, 0, 4, 3, 1, 0]
G = [[0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1],
     [1, 1, 1, 0, 1, 0]]

# [0, 4, 5, 6, 2, 5, 1, 6, 7, 3, 2, 1, 0]
G = [[0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]

# [0, 4, 5, 3, 4, 2, 0, 3, 1, 0]
G = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1],
     [0, 0, 0, 1, 1, 0]]

# [0, 4, 5, 2, 4, 1, 5, 3, 2, 1, 0]
#G = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1],
    # [0, 1, 1, 1, 1, 0]]

# None
#G = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

# None
#
#G = []

#n = 1001
#G = [[0 if i == j else 1 for i in range(n)] for j in range(n)]

# not all degrees even
#G = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

# not connected
#G = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]]
k=1001
'''G = [[1 for _ in range(k)] for _ in range(k)]
for i in range(k):
  G[i][i] = 0'''
euler(G)