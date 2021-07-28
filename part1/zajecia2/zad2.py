from math import inf


def merge_sort(arr):
    def sub_merge_sort(arr, p, r):
        if p < r:
            q = (p + r) // 2
            sub_merge_sort(arr, p, q) #wywołanie dla lewej podtablicy
            sub_merge_sort(arr, q + 1, r) #wywołanie dla prawej podtablicy
            merge(arr, p, q, r) #scalanie posortowanych podtablic

    def merge(arr, p, q, r):
        global cnt
        n1 = q - p + 1 #długość podtablicy, +1 wynika z indeksowania tablicy od 0
        n2 = r - q
        L = [None]*(n1+1) #dodatkowe miejsce w tablicy dla wartownika
        R = [None]*(n2+1)
        for i in range(n1): #kopiowanie podtablicy lewej
            L[i] = arr[p+i]
        for j in range(n2): #kopiowanie podtablicy prawej
            R[j] = arr[q+j+1] #+1 bo q jest wynikiem dzielenia calkowitego, a prawa tablica zaczyna sie indeks dalej

        L[n1] = inf #rozwiazanie z wartownikiem, przyspiesza działanie, inspirowane z książki "Wprowadzenie do algorytmów"
        R[n2] = inf

        i = j = 0
        for k in range(p,r+1): #r + 1, bo chcemy przeiterować do r
            if L[i] <= R[j]: #porównywanie elementów lewej i prawej podtablicy
                arr[k] = L[i] #przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
                i += 1
            else:
                arr[k] = R[j] #przypisanie do właściwego miejsca w tablicy, w posortowanej kolejności
                if L[i] != inf and R[j] != inf: #rozwiązanie zadania
                    cnt += n1 - i
                j += 1

    p = 0 #pierwszy indeks
    r = len(arr)-1 #ostatni indeks
    sub_merge_sort(arr,p,r)

    return cnt

cnt = 0
A = [3, 2, 1, 0, 5]
print(merge_sort(A))
cnt = 0
A = [1,2,3,4,5,6]
print(merge_sort(A))
cnt = 0
A = [6,5,4,3,2,1]
print(merge_sort(A))