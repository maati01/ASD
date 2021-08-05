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

def anagram(A,B):
    n = len(A)
    m = len(B)

    arr1 = [0]*n
    arr2 = [0]*n

    if n != m:
        return False

    for i in range(n):
        arr1[i] = ord(A[i])
        arr2[i] = ord(B[i])

    arr1 = counting_sort(arr1)
    arr2 = counting_sort(arr2)

    for i in range(n):
        if arr1[i] != arr2[i]:
            return False

    return True

A = 'AbcdEf'
B = 'bAdcfE'
C = 'AbcdrEf'
D = 'AbcdREf'

print(anagram(A,B))
print(anagram(C,D))