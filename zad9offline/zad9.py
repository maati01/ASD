from copy import deepcopy


def min_cycle( G ):
  """miejsce na Twoją implementację!"""
  return []
  
  
  
  
  
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
  
