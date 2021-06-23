from random import shuffle, seed,randint

global licznik;
# insertion sort dzialajacy na fragmencie tablicy
def insertion_sort(A, left, right):
    for j in range(left + 1, right + 1):
        key = A[j]
        i = j - 1
        while i >= left and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


# zmodyfikowana wersja zwyklega partition, przyjmujaca element, wedlug ktorego dzieli tablice
# gdyby elementy w tablicy nie byly parami rozne, nalezaloby zaimplementowac three-way partition
def partition(A, left, right, x):
    for i in range(left, right):
        if A[i] == x:
            A[right], A[i] = A[i], A[right]
            break

    x = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i


# funkcja "dzieli" podana tablice na 5-elementowe zbiory, sortuje
# wybiera miediany i zamienia je miejscami z kolejnymi elementami tablicy
# zaczynajac od pierwszego
def magic_medians(A, left, right):
    num_of_el = right - left + 1

    i = 0  # ilosc znalezionych median
    while i < num_of_el // 5:  # podzial, sortowanie, znalezienie median
        l_five = left + i * 5
        r_five = l_five + 4
        insertion_sort(A, l_five, r_five)
        A[left + i], A[(l_five + r_five) // 2] = A[(l_five + r_five) // 2], A[left + i]
        i += 1
        licznik +=1;

    if i * 5 < num_of_el:  # mediana z pozostalosci (gdy tab.length % 5 != 0)
        l_five = left + i * 5
        r_five = left + i * 5 + num_of_el % 5 - 1
        insertion_sort(A, l_five, r_five)
        A[left + i], A[(l_five + r_five) // 2] = A[(l_five + r_five) // 2], A[left + i]
        i += 1

    if i == 1:  # gdy zostala jedna zwraca
        return A[left]
    else:  # mediana z median
        return magic_medians(A, left, left + i - 1)


def select(A, left, right, k):
    if left <= k <= right:
        med_of_med = magic_medians(A, left, right)  # znalezienie mediany

        pos = partition(A, left, right, med_of_med)  # partionion wedlug znalezionej mediany
        if pos == k:
            return A[pos]
        if pos > k:
            return select(A, left, pos - 1, k)  # szukany element w "lewej" czesci tablicy

        return select(A, pos + 1, right, k)  # szukany element w "lewej" czesci tablicy

    return 99999999


def linearselect(A, k):
    return select(A, 0, len(A) - 1, k)


seed(42)

n = 0
for i in range(n):
    A = list(range(n))
    shuffle(A)
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
print(licznik);