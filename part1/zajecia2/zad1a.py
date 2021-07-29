from math import inf


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + j + 1]

    L[n1] = inf
    R[n2] = inf

    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def natural_series(A):
    n = len(A)
    flag = True
    index = []

    for i in range(1, n):
        if A[i - 1] < A[i]:
            index.append(i)

    k = len(index)

    for i in range(k-1):
        merge(A,0,index[i],index[i+1])

    return A


A = [1, 2, 56, 57, 3, 3, 4, 5, 9, 10, 99, 109, -3, -2, 2000]
print(natural_series(A))
