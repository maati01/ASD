def counting_sort(A,y): #counting sort który przyjmuje również indeks tupla po którym ma sortować z uzyciem ord który zamienia chary na wartosci
    B = [0]*len(A)
    max_k = 0
    for i in range(len(A)):
        if ord(A[i][y]) > max_k:
            max_k = ord(A[i][y])
    def sub_counting_sort(A,B,k):
        x = len(A)
        C = [0]*(k+1) #tablica długości max_k
        for j in range(x): #jeśli wartość występuje zliczamy ją
            C[ord(A[j][y])] += 1

        for i in range(1,k+1): #sumujemy popednia i nastepna wartość, aby wiedzieć ile miejsc jest zajętych przed obecną wartością
            C[i] += C[i-1]

        for k in range(x-1,-1,-1):
            B[C[ord(A[k][y])]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[ord(A[k][y])] = C[ord(A[k][y])] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie

    sub_counting_sort(A,B,max_k)

    return B

def sortString(A):
    n = len(A)
    B = []
    maksimum = len(A[0])
    minimum = len(A[0])

    for i in range(1,n):
        if maksimum < len(A[i]):
            maksimum = len(A[i])
        if minimum > len(A[i]):
            minimum = len(A[i])

    buckets = []

    for j in range(maksimum): #tworze buckety
        buckets.append([])

    for k in range(n): #dodaje stringi w odpowednie miejsca
        buckets[len(A[k])-minimum].append(A[k])

    k = 0
    j = 0
    for i in range(maksimum-1,-1,-1):
        while len(buckets[i]) != k and len(buckets[i]) != 0: #wkładam nadluzszy bucket, drugi nadłuzszy itd..
            B = [buckets[i][k]] + B #dodaje lementy za początek aby zachować porządek leksykograficzny
            k += 1
        while j < i + 1:
            B = counting_sort(B,j) #sortuje go wzgledem ostatniego, przedostaniego itd.. indeksu
            j += 1
        j = 0
        k = 0
    return B

tab = ["aab","aac","aaa","a","ab","bbbbbb","b","xx","assag","b","c","aaaaaaaaaaaaaaaaaaaaa"]
#tab = ["ac","b","c","a","bbb"]
print("pritnt sorted",sortString(tab))
print("pritnt sorted",sorted(tab))


