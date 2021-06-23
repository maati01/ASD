def counting_sort(A):
    B = [0]*len(A)
    max_k = 0
    for i in range(len(A)):
        if A[i] > max_k:
            max_k = A[i]
    def sub_counting_sort(A,B,k):
        x = len(A)
        C = [0]*(k+1) #tablica długości max_k
        for j in range(x): #jeśli wartość występuje zliczamy ją
            C[A[j]] += 1

        for i in range(1,k+1): #sumujemy popednia i nastepna wartość, aby wiedzieć ile miejsc jest zajętych przed obecną wartością
            C[i] += C[i-1]

        for k in range(x-1,-1,-1):
            B[C[A[k]]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[A[k]] = C[A[k]] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie


    sub_counting_sort(A,B,max_k)

    return B

#test.test_sort(counting_sort,10,100,(0,1000),True)


#wersja Romana
# time complexity: n + m*n
# space complexity: m
def counting_sort1(A, _min, _max):
  m = abs(_max - _min) + 1 #ustalam długośc tablicy
  n = len(A)
  O = [0]*m # occurances

  for i in range(n):
    O[A[i]-_min] += 1 #min jest "0", wiec przesuwam index w prawo

  i = 0
  for j in range(m):
    while O[j] > 0:
      A[i] = _min + j #dodaje wartość do juz wyjsciowej tablicy
      O[j] -= 1 #zmniejszam wystepopwanie
      i += 1 #przesuwam index w prawo

  return A


# time complexity: n + m-1 + n = 2*n + m - 1
# space complexity: n + m
#wersja z cormena z uwzglednieniem <0
def counting_sort2(A, _min, _max):
  m = abs(_max - _min) + 1
  n = len(A)
  O = [0]*m # occurances

  for i in range(n):
    O[A[i]-_min] += 1 #przesuniecie wzgledem min

  for i in range(1, m):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    B[O[A[i]-_min]-1] = A[i] #przesuniecie wzgledem min
    O[A[i]-_min] -= 1 #przesuniecie wzgledem min

  return B


