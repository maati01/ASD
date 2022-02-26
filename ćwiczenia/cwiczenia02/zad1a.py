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

def find_indexes(A,p):
    n = len(A)
    q = None
    r = None
    for i in range(p+1, n-1):
        if q is None and A[i] < A[i-1]:
            q = i
        elif q is not None and A[i] < A[i-1]:
            r = i

    if q is not None and r is None:
        r = n - 1

    return q , r

def natural_series(A):
    n = len(A)
    while True:
        p = 0
        while True:
            q, r = find_indexes(A, p)
            if p == 0 and q is None:
                return A

            if q is None:
                break



            merge(A,p,q - 1,r - 1)

            p = r


A = [1, 2, 56, 57, 3, 3, 4, 5, 9, 10, 99, 109, -3, -2, 2000]
print(natural_series(A))
print(sorted(A))
B = [-9,-8,-7,-6,-4]
print(natural_series(B))
print(sorted(B))
C = [1]
print(natural_series(C))
print(sorted(C))
D = [1,2,3,1,2,3]
print(natural_series(D))
print(sorted(D))
E = [3,2,1,3,2,0,-1,-2,9]
print(natural_series(E))
print(sorted(E))

