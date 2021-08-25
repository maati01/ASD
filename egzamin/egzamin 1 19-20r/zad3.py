from zad3testy import runtests
import math

#zwykły bucket sort
#zazkres bucketów od 1 do a
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


def find_bucket(A, n, minimum, maximum, i): #funkcja przydziela bucketa uwzględniająć liczby ujemne
    _i = int((A[i] - minimum) / (maximum - minimum) * n)
    if _i == n: _i -= 1

    return _i

def fast_sort(tab, a):
    n = len(tab)
    if n == 1 or n == 0:
        return tab
    B = []
    indeks = 0

    minimum = 1
    maximum = a

    for i in range(len(tab)): #tworze buckety
        B.append([])

    for i in range(n):
        B[find_bucket(tab, n, minimum, maximum, i)].append(tab[i]) #dodaje element do odpowiedniego bucketa

    for i in range(n): #sortowanie pojedynczych bucketów
        insertion_sort(B[i])

    for i in range(n): #polaczenie juz posortowanych bucketów, liniowe bo buckety maja po kilka elementów
        for j in range(len(B[i])):
            tab[indeks] = B[i][j]
            indeks += 1

    return tab

runtests( fast_sort )
