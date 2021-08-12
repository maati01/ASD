# f(i) - minimalna liczba monet do wydania i kwoty
# f(i) - min(f(i - A[j]) + 1, f(i - A[j])), gdzie j przebiega po wszystkich monetach

from math import inf


def coins(A, x):
    A.sort()
    n = len(A)
    F = [inf] * (x + 1)
    F[0] = 0
    parents = [0] * (x + 1)

    for i in range(n):
        F[A[i]] = 1
        parents[A[i]] = A[i]

    for i in range(x + 1):
        for j in range(n):
            if i >= A[j]:
                if F[i - A[j]] + 1 < F[i]:
                    parents[i] = A[j]
                F[i] = min(F[i - A[j]] + 1, F[i])

    if F[x] == inf:
        return False

    i = x
    while i != 0:
        print(parents[i], end=' ')
        i -= parents[i]

    print()

    return F[x]


M = [1, 5, 8]
x = 15
#M = [1, 5, 8, 100]
#x = 4001

print(coins(M, x))
