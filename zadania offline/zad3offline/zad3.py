from random import randint, shuffle, seed

def insertion_sort(arr, left,
                   right):  # insertion sort sluzy do posortowania "piątek", mała ilość gwarantuje liniowy czas, zmodyfikowany tak aby sortował okreslony fragment tablicy
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def get_median(left, right):  # funkcja pozwala wyznaczyć indeks mediany
    return (left + right) // 2  # biorę mniejsza mediane gdy jest parzysta ilosc


def partation(A, left, right,x):  # funkcja partation taka jak w quicksortcie, ale szuka indeks dla mediany i zamienia ją z ostanim elementem
    for i in range(left, right):
        if A[i] == x:
            A[right], A[i] = A[i], A[right]
            break
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1


def linearselectv2(A, left, right, k):
    if (k >= left and k <= right):  # warunek końca
        n = len(A)
        indeks = 0
        last = 0
        rest = n % 5  # gwarancja stworzenia ciagów o dlugosci 5, ewentualny ciąg < 3 rozpatrze osobno
        for i in range(left, right - rest - 4, 5): #przeskakuje co 5 w celu sprawdzenia ciagów długości 5
            insertion_sort(A, i, i + 4)  # sortuje podciągu długosci 5
            A[left + indeks], A[get_median(i, i + 4)] = A[get_median(i, i + 4)], A[left + indeks]  # zamieniam mediany w kolejnych piątkach z początkowymi indeksami w tablicy aby je przechowywac i nie tworzyć dodatkowej tablicy
            indeks += 1
            last = i

        if rest != 0:  # sortuje ewentualny podciag <5
            insertion_sort(A, last + 5, last + 5 + rest - 1)  # dodaje 5 zeby wyrównać ostanią iterację fora wyżej
            A[indeks], A[get_median(last + 5, last + rest + 4)] = A[get_median(last + 5, last + rest + 4)], A[indeks]
            indeks += 1

        if indeks == 1: #jesli jest jedna mediana
            medOfMed = A[left]
        else:
            medOfMed = linearselectv2(A, left, left + indeks - 1,indeks // 2)  # wywołanie rekurencyjne aby wyznaczyć medianę median

        pos = partation(A, left, right, medOfMed)  #partation dla znalezionej mediany

        if (pos == k): #znaleziona mediana
            return A[pos]

        if (pos > k):
            return linearselectv2(A, left, pos - 1, k) #przypadek pierwszy z zakresu do mediany

        return linearselectv2(A, pos + 1, right, k) #przypadek drugi > od mediany

    return 10 ** 100


def linearselect(A, k):
    left = 0
    right = len(A) - 1
    return linearselectv2(A, left, right, k)


seed(42)

n = 120
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")

###test Pawła
from time import time



def test_sort():
    seed(42)
    rr = (-10 ** 5, 10 ** 5)
    n = 10 ** 6
    m = 5
    print_res = False

    for i in range(m):
        t = [randint(rr[0], rr[1]) for _ in range(n)]
        expected_res = sorted(t)

        k = randint(0, n - 1)
        'k=30'
        expected = expected_res[k]

        if print_res:
            print('sorted_input:   ', expected_res)

        start = time()
        q = linearselect(t, k)
        stop = time()
        if print_res: print('output:  ', q, ' expected:  ', expected)

        res = 'INCORRECT'
        if q == expected:
            res = 'CORRECT'

        print('result:  ', res)
        print('time:    ', stop - start, '\n')

        if res == 'INCORRECT':
            break

test_sort()

