def counting_sort(A,y): #counting sort który przyjmuje również indeks tupla po którym ma sortować
    B = [0]*len(A)
    max_k = 0
    for i in range(len(A)):
        if A[i][y] > max_k:
            max_k = A[i][y]
    def sub_counting_sort(A,B,k):
        x = len(A)
        C = [0]*(k+1) #tablica długości max_k
        for j in range(x): #jeśli wartość występuje zliczamy ją
            C[A[j][y]] += 1

        for i in range(1,k+1): #sumujemy popednia i nastepna wartość, aby wiedzieć ile miejsc jest zajętych przed obecną wartością
            C[i] += C[i-1]

        for k in range(x-1,-1,-1):
            B[C[A[k][y]]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[A[k][y]] = C[A[k][y]] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie

    sub_counting_sort(A,B,max_k)

    return B

def SumSort(A,B,n):
    B = [0]*(n*n)
    tab = [0]*n
    j = 0
    suma = 0
    p = 0
    for i in range(1,n*n+1):
        suma += A[i-1]
        if i%n == 0 and i != 0:
            tab[j] = (p,i-1,suma) #tworze krotke z indeksem pierwszym i ostatnim sumy oraz sama sumą
            p = i
            j += 1
            suma = 0

    tab = counting_sort(tab,2) #sortuje wzgledem sumy

    k = 0
    for i in range(n):
        for j in range(tab[i][0],tab[i][1]+1): #przepisuje wartosci miedzy indeksami które przechowuje krotka(wartosci z tablicy A) do B
            B[k] = A[j]
            k += 1

    return B

from random import randint
n = 5
A = [randint(0, 10) for _ in range(n*n)]
B = [0 for _ in range(n*n)]

print(SumSort(A,B,n))