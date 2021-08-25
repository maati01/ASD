from zad3testy import runtests
import math

#zwykły bucket sort
#x ma rozklad jednostajny
#trzeba znalezc krancowe x zeby storzyc buckety
#skorzystam z x = log(a,tab[i])
#szukamy buckeity na podstawie powyzszego rownania
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr


def find_bucket(A, n, minimum, maximum, i,a): #funkcja przydziela bucketa uwzględniająć liczby ujemne
    _i = int((math.log(A[i],a) - minimum) / (maximum - minimum) * n)
    if _i == n: _i -= 1

    return _i

def fast_sort(tab, a):
    n = len(tab)
    if n == 1 or n == 0:
        return tab
    B = []
    indeks = 0

    minimum = math.log(min(tab),a)
    maximum = math.log(max(tab),a)


    for i in range(len(tab)): #tworze buckety
        B.append([])

    for i in range(n):
        B[find_bucket(tab, n, minimum, maximum, i,a)].append(tab[i]) #dodaje element do odpowiedniego bucketa

    for i in range(n): #sortowanie pojedynczych bucketów
        insertion_sort(B[i])

    for i in range(n): #polaczenie juz posortowanych bucketów, liniowe bo buckety maja po kilka elementów
        for j in range(len(B[i])):
            tab[indeks] = B[i][j]
            indeks += 1

    return tab

runtests( fast_sort )
