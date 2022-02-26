from copy import deepcopy
from math import inf

#dla każdego wierzchołka wywołuje djikstre sprawdzając najmniejsze ścieżkli między wierzchołkami
#dla V wierzchołków i złożoności czasowej dijkstry O(V^2) złożoność operacji wynosi O(V^3)
#szukam najkrótszych scieżek miedzy wierzchołkami od i do j oraz od i do k
#sprawdzam czy występuje wierzchołek k który ma połączenie z j oraz jego rodzic jest inny od rodzica j
#to gwarantuje że nie wróce tą samą scieżką do wierzchołka i
#tak uzyskuje najkrótszy cykl od  ze ścieżek od i do j, od i do k gdzie j oraz k mają krawędz, cała operacja ma złozoność O(V^3)
#wywołania dijkstry oraz petli i,j,k sa niezależne więc cały algorytm ma złożoność O(V^3)


def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind

def dijkstra(G,v):#dijkstra z dwiema petlami n wiec zlozonosc O(n^2)
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != -1 and d[i] > d[v] + G[v][i]: #relaksacja
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return d,parents

def min_cycle( G ):
    min = inf
    n = len(G)
    F = [] #tablica trzyma dystanse miedzy wierzchołkiem s i v
    new_parents = [] #tablica trzyma rodziców dla każdego wywołania dijkstry
    result = []
    temp_result = []
    temp = 0

    for i in range(n): #odpalam dijkstre dla kazdego wierzchołka zapisujac najkrótsze ścieżki i rodziców
        d,parents = dijkstra(G,i)
        F.append(d)
        new_parents.append(parents)

    for i in range(n): #szukam najkrótszej ścieżki od i do j, oraz od i do k, gdzie j oraz k mają bezpośrednią krawędź
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k: #nie mogą być to te same wierzchołki
                    if F[i][j] != inf and F[i][k] != inf and G[j][k] != -1 and new_parents[k][i] != new_parents[j][i] and min > F[i][j] + F[i][k] + G[j][k]:
                        min = F[i][j] + F[i][k] + G[j][k] #w warunku wyżej sprawdzam czy isnieje ścieżka miedzy i -> j, i -> k, oraz czy rodzic nie jest wspólny
                        temp = (i,j,k)                    #sprawdzam czy jest krawędź j -> k,jestli tak to istnieje cykl i go minimalizuje

    if temp != 0: #odtwarzenie wyniku
        i, j, k = temp
        temp2 = k
        result.append(j)
        while j != i:
            result.append(new_parents[i][j]) #odtwrzam sciezke od j do i
            j = new_parents[i][j]
        while k != i: #odtwrzam ścieżke od k do i
            temp_result.append(new_parents[i][k])
            k = new_parents[i][k]
        ind = 0
        while temp_result[ind] != i: #łącze ścieżki tak by tworzyły cykl
            result.append(temp_result[ind])
            ind += 1
        result.append(temp2)

    return result
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
