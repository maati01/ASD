from random import randint, seed
from math import inf
#Mateusz Powęska



def mergesort(T):
  def sub_merge_sort(T, p, r):
    if p < r:
      q = (p + r) // 2
      sub_merge_sort(T, p, q)  # wywołanie dla lewej podtablicy
      sub_merge_sort(T, q + 1, r)  # wywołanie dla prawej podtablicy
      merge(T, p, q, r)  # scalanie posortowanych podtablic

  def merge(arr, p, q, r):
    n1 = q - p + 1  # długość podtablicy, +1 wynika z indeksowania tablicy od 0
    n2 = r - q
    L = [None] * (n1 + 1)  # dodatkowe miejsce w tablicy dla wartownika
    R = [None] * (n2 + 1)
    for i in range(n1):  # kopiowanie podtablicy lewej
      L[i] = arr[p + i]
    for j in range(n2):  # kopiowanie podtablicy prawej
      R[j] = arr[q + j + 1]  # +1 bo q jest wynikiem dzielenia calkowitego, a prawa tablica zaczyna sie indeks dalej

    L[n1] = inf  # rozwiazanie z wartownikiem, przyspiesza działanie, inspirowane z książki "Wprowadzenie do algorytmów"
    R[n2] = inf

    i = j = 0
    for k in range(p, r + 1):  # r + 1, bo chcemy przeiterować do r
      if L[i] <= R[j]:  # porównywanie elementów lewej i prawej podtablicy
        arr[k] = L[i]  # przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
        i += 1
      else:
        arr[k] = R[j]  # przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
        j += 1

  p = 0  # pierwszy indeks
  r = len(T) - 1  # ostatni indeks
  sub_merge_sort(T, p, r)

  return T

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")