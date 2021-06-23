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

def reverse_counting_sort(A,y): #counting sort który przyjmuje również indeks tupla po którym ma sortować
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

        for k in range(x):
            B[C[A[k][y]]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[A[k][y]] = C[A[k][y]] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie

    sub_counting_sort(A,B,max_k)

    return B

def pretty_sort(T):
    n = len(T)
    digits = [0]*9
    once = 0
    multiple = 0
    for i in range(n):
        x = T[i]
        while x > 0:
            digits[x%10] += 1
            x //= 10
        for j in range(9):
            if digits[j] == 1 :once += 1
            if digits[j] > 1 : multiple += 1
        T[i] = (T[i],once,multiple) #tupla która przyjmuje liczbe, cyfyr jednokrotne i wielokrotne z minusem(aby po sortowaniu były malejąco)
        once = 0
        multiple = 0
        digits = [0] * 9

    T = counting_sort(T,2)
    T = reverse_counting_sort(T,1)

    ind = 0
    tab= [0]*n
    for i in range(n-1,-1,-1):
        tab[ind] = T[i][0]
        ind += 1

    return tab

'''print(pretty_sort([67333,2344,114577,1266,455,123]))
print(pretty_sort([455,123]))
print(pretty_sort([114577,1266]))
print(pretty_sort([2344,67333]))
print(pretty_sort([67333,2344]))'''
test = [3322, 1266, 114577, 123, 455, 2344, 67333, 1234455, 12344, 12, 134, 12, 13, 432, 543, 5434, 22]
print(pretty_sort(test))