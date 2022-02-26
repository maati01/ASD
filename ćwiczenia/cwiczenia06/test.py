from math import inf
from random import randint, seed

seed(123)

def frog(A):
    n = len(A)
    F = [[inf] * n for _ in range(n)]
    F[min(A[0], n - 1)][0] = 0

    for i in range(n - 1):
        for e in range(n):
            if F[e][i] != inf:
                for x in range(1, n - i):
                    if x > e:
                        break

                    new_e = min(n - 1, e - x + A[i + x])
                    F[new_e][i + x] = min(F[new_e][i + x], F[e][i] + 1)

    result = inf
    for i in range(n):
        print(F[i])
    for i in range(n - 1):
        result = min(result, F[i][n - 1])

    # [print(x) for x in F]
    print(result)


'''A = [randint(0, 30) for _ in range(200)]
print(A)
frog(A)'''

#A = [1,2,3,4,5]
A = [1,2,2,2,2,2]
#A = [2,2,1,0,0,0]
#A = [4,5,2,5,1,2,1,0]
frog(A)
# frog([20, 0, 0, 0, 0, 0, 0])