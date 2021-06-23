from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

def qsort( L ):
  def wardens(L): #dodanie wartowników na początku i końcu
    curr = L
    w_start = Node() #wartownik początkowy
    w_end = Node() #wartownik końcowy
    w_start.value = "*" #dla wizualizacji
    w_end.value = "*"
    w_start.next = L
    while curr.next != None:
      curr = curr.next
    curr.next = w_end

    return w_start,w_end
  def remove_warden(L): #funkcja usuwa wartownika z końca
    curr = L
    while curr.next.value != "*":
      curr = curr.next
    curr.next = None



  def quicker_sort(w_start,w_end):
    prev_w = w_start #wskaźnik pomocniczny(aby nie zgubic połączenia miedzy piwotem a elementem poprzedzającym go), początkowo wskazuje na wardena
    prev = w_start.next #ustalam preva na pierwszy element po wartowniku
    curr = w_start.next.next ##zaczynam od elementu po previe
    start_p = w_start.next #piwot początkowy
    end_p = w_start.next #piwot końcowy

    if curr == w_end: #warunek końca
      return

    while curr != w_end:
      if curr.value < start_p.value:
        prev.next = curr.next #prev wskazuje teraz na element za currem
        curr.next = start_p #curra przepinam aby wskazywał na piwota
        prev_w.next = curr  #wskaźnik pomocniczy wskazuje teraz na curra
        prev_w = curr #wskaźnikiem pomocniczym staje sie teraz curr
        curr = prev.next #curra przestawiam na nastepny element do porównania
      elif curr.value == start_p.value and end_p != curr:
        prev.next = curr.next #przepinam preva na element za currem
        curr.next = end_p.next #teraz curr wskazuje na element po drugim piwocie
        end_p.next = curr #drugi piwot wskazuje teraz na curra
        end_p = curr #przestawiam drugiego piwota za curra tak aby stawał się ostatnim elementem tych samych wartości
        curr = prev.next #przesuwam curra na nastepny element do porównania
      else: #wartosc jest wieksza od piwota wiec jej nie ruszam, jedynie przesuwam curra i preva
        curr = curr.next
        prev = prev.next

    if w_start.next != start_p: #warunek aby nie sprawdzać pustych list
      quicker_sort(w_start,start_p)
    if end_p.next != w_end: #warunek aby nie sprawdzać pustych list
      quicker_sort(end_p,w_end)

    return



  w_start,w_end = wardens(L) #tworze wartowników dla orientacji
  quicker_sort(w_start,w_end)
  remove_warden(L) #usuwam ostatniego wartownika

  return w_start.next #zwracam wskaźnik na element po wartowniku aby go zgubić



def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")


seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")