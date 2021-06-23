from copy import deepcopy
from collections import deque

#dla każdego wierzchołka mam maksymalnie n wywołań pętli więc złożoność obliczeniowa algorytmu wynosi w pesymistycznym przypadku n^2
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

    for i in range(n): #jesli po wywołaniu bfsa wszystkie krawedzie za odwiedzone do graf jest spójny
        if visited[i] == False:
            return False

    return True


def check(G):  # funkcja sprawdza parzystość wierzchołków i ich wymaganą ilość
    n = len(G)
    cnt = 0
    if n < 4:
        return False

    for i in range(n):
        for j in range(n): #zliczam ilość krawędzi
            if G[i][j] == 1:
                cnt += 1
        if cnt % 2 != 0:
            return False
        cnt = 0

    return True


def euler(G):
    if not check(G):  # sprawdzam parzystosc i ilosc wierzchołków, n^2
        return None

    if not BFS(G, 0):  # sprawdzam spójność, zlozonosc BFSa to n^2
        return None

    n = len(G)
    visited = [False for _ in range(n)]  # tablica okresla czy wierzchołek został przetworzony
    tab = []  # stos
    result = []  # tutaj tworze wynik
    last = [0] * n  # tablica trzyma dla kazdego wierzchołka numer wierzchołka na którym pętla skończyła sprawdzać, poprawia to złożoność i zabezpiecza przed sytacja n^3
    tab.append(0)  # dodaje do stosu wierzchołek od którego zaczynam
    s = 0 #zaczynam od wierzchołka 0
    while (len(tab)):  # dopóki mam stos szukam wierzchołków do cyklu
        if visited[s] != -1:  # sprawdzam wierzchołek gdy ma jeszcze krawedzie
            for i in range(last[s], n):  # sprawdzam od ostatniego wierzchołka na którym skończyłem, maksymalna złożoność ogliczeniowa dla grafu pełnego to n^2
                if G[s][i] == 1:  # jesli ma krawedz to ją sprawdzam
                    G[s][i] = -1  # usuwam krawedz w obie strony(-1 oznacza usuniecie krawedzi)
                    G[i][s] = -1
                    last[s] = i  # zapamietuje do którego wierzchołka sprawdziłem krawędz z danym wierzchołkiem
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
        for j in range(n):  # przywracam macierz do stanu pierwotnego, dzieku czemu nie potrzebuje dodatkowej pameici
            if G[i][j] == -1:
                G[i][j] = 1

    if result[0] == result[len(result) - 1]:  # jeśli wróciłem do miejsca od którego zaczynał oznacza to że mam cykl Eulera
        return result
    else:
        return None

  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")