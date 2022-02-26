from testy import test

def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr


def find_bucket(A, n, minimum, maximum, i): #funkcja przydziela bucketa uwzględniająć liczby ujemne
    _i = int((A[i] - minimum) / (maximum - minimum) * n)
    if _i == n: _i -= 1

    return _i

def bucket_sort(A):
    n = len(A)
    if n == 1 or n == 0:
        return A
    B = []
    indeks = 0

    minimum = A[0]
    maximum = A[0]

    for i in range(n): #szukam max i min, ktore beda potrzebne do okreslenia odpowiednich przedziałów dla bucketów
        if maximum < A[i]:
            maximum = A[i]
        if minimum > A[i]:
            minimum = A[i]


    for i in range(len(A)): #tworze buckety
        B.append([])

    for i in range(n):
        B[find_bucket(A, n, minimum, maximum, i)].append(A[i]) #dodaje element do odpowiedniego bucketa

    for i in range(n): #sortowanie pojedynczych bucketów
        insertion_sort(B[i])

    for i in range(n): #polaczenie juz posortowanych bucketów, liniowe bo buckety maja po kilka elementów
        for j in range(len(B[i])):
            A[indeks] = B[i][j]
            indeks += 1

    return A


test.test_sort(bucket_sort,10**3,10,(-10**4,10**4),True)
#print(bucket_sort([31, 3, -29, -18, 7, 7, -37, -21, -35, -17]))
