from queue import PriorityQueue
from math import inf
from copy import deepcopy

#O(V + ElogV)
#algorytm przechodzi po krawedziach z kazdego wierzchołka
#sprawdza wartość przepływu w wierzchołku
#maksymalizuje przepływ po wierzchołku z którego wychodzi, do którego wchodzi i krawędzi
#dzięki wrzucaniu do kolejki priorytetowej przepływów z minusem, ściągamy zawsze najwiekszy przepływ
#sprawdzam dla kazdego wierzchołka V wszystkie jego krawędzie, put zajmuje logV stąd złożoność O(V + ElogV)

def dijkstra(G, v): #zmodyfikowana dijkstra
  n = len(G)
  d = [inf] * n  # przepłw
  parents = [None] * n
  processed = [False] * n  # wierzchołki przetworzone
  Q = PriorityQueue()
  Q.put((-d[v], v))  # krotka trzyma akutalny dystans i indeks, wrzucam z minusem zeby miec jak najwiekszza przepustowość
  while not Q.empty():
    temp = Q.get()  # priority queue posortowane po oszacowanych dystansach
    u = temp[1]
    if not processed[u]:  # sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
      for s in G[u]: #sprawdzam wszystkie krawędzie więc O(E)
        if d[s[0]] > min(d[u], s[1]) and d[s[0]] == inf:  # minmimalna przepustowość z wierzchołka obecnego i poprzedniego
          d[s[0]] = min(d[u],s[1])  # jesli natrafiłem na inf to znaczy że wchodzę pierwszy raz i nadpisuje min z krawedzi
          parents[s[0]] = u  # i wierzchołka z którego wyszedłem
          Q.put((-d[s[0]], s[0]))
        elif d[s[0]] < min(d[u],s[1]):  # gdy w wierzchołku jest mniejsza wartość to znaczy że mogę zwiekszyc przepustowość
          d[s[0]] = min(d[u], s[1])
          parents[s[0]] = u
          Q.put((-d[s[0]], s[0]))

      processed[u] = True

  return d, parents

def max_extending_path( G, s, t ):
    d,parents = dijkstra(G,s)
    res = []
    if d[t] != inf: #isteniej minimalny przepływ
        res.append(t)
        while(parents[t] != None): #odtowrzenie wyniku
            res.append(parents[t])
            t = parents[t]

        return res[::-1]

    return res

  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
