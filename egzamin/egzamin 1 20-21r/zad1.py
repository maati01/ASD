from zad1testy import runtests
from math import inf

#niekoniecznie musi byc sortowanie stabilne
#wystarczy porównywać krotki np. quick sortcie

def merge_sort(arr):
    def sub_merge_sort(arr, p, r):
        if p < r:
            q = (p + r) // 2
            sub_merge_sort(arr, p, q) #wywołanie dla lewej podtablicy
            sub_merge_sort(arr, q + 1, r) #wywołanie dla prawej podtablicy
            merge(arr, p, q, r) #scalanie posortowanych podtablic

    def merge(arr, p, q, r):
        n1 = q - p + 1 #długość podtablicy, +1 wynika z indeksowania tablicy od 0
        n2 = r - q
        L = [None]*(n1+1) #dodatkowe miejsce w tablicy dla wartownika
        R = [None]*(n2+1)
        for i in range(n1): #kopiowanie podtablicy lewej
            L[i] = arr[p+i]
        for j in range(n2): #kopiowanie podtablicy prawej
            R[j] = arr[q+j+1] #+1 bo q jest wynikiem dzielenia calkowitego, a prawa tablica zaczyna sie indeks dalej

        L[n1] = inf,inf #rozwiazanie z wartownikiem, przyspiesza działanie, inspirowane z książki "Wprowadzenie do algorytmów"
        R[n2] = inf,inf

        i = j = 0
        for k in range(p,r+1): #r + 1, bo chcemy przeiterować do r
            if L[i][0] <= R[j][0]: #porównywanie elementów lewej i prawej podtablicy
                arr[k] = L[i] #przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
                i += 1
            else:
                arr[k] = R[j] #przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
                j += 1

    p = 0 #pierwszy indeks
    r = len(arr)-1 #ostatni indeks
    sub_merge_sort(arr,p,r)

    return arr


def chaos_index(T):
    n = len(T)

    for i in range(n):
        T[i] = (T[i], i)

    T = merge_sort(T)

    k = -inf
    for i in range(n):
        if abs(T[i][1] - i) > k:
            k = abs(T[i][1] - i)

    return k


print(chaos_index([1, 2, 1, 2, 1, 2]))
runtests(chaos_index)
