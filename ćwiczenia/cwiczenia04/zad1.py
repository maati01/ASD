#Dana jest tablica zawierająca n liczb z zakresu [0...n^2-1]. Napisz algorytm, który posortuje taką tablicę w czasie O(n).
#liczba w psotaci k = an + b

def modulo(k,n):
    temp = k%n
    return temp

def divide(k,n):
    temp = k//n
    return temp

def counting_sort(A,func):
    x = len(A)
    B = [0]*len(A)
    max_k = 0
    for i in range(len(A)):
        if func(A[i],x) > max_k:
            max_k = func(A[i],x)
    def sub_counting_sort(A,B,k,func):
        x = len(A)
        C = [0]*(k+1) #tablica długości max_k
        for j in range(x): #jeśli wartość występuje zliczamy ją
            C[func(A[j],x)] += 1

        for i in range(1,k+1): #sumujemy popednia i nastepna wartość, aby wiedzieć ile miejsc jest zajętych przed obecną wartością
            C[i] += C[i-1]

        for k in range(x-1,-1,-1):
            B[C[func(A[k],x)]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[func(A[k],x)] = C[func(A[k],x)] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie

    sub_counting_sort(A,B,max_k,func)

    return B

def radix(A):
    B = counting_sort(A,modulo) #tablica posortowana po %
    return counting_sort(B,divide) #tablica posortowana po //


print(radix([11,10,55,32,12512,5125,121,441,523,2,1,0]))
print(radix([5,4,3,2,1]))