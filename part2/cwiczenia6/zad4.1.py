#f(i,j) - minimalna liczba skoków aby dostać się do i mając dokładnie j energii
#f(i,j) = min f(k, j - k - A[i]) + 1

from math import inf

def frog(A):
    n = len(A)
    sum_energy = sum(A) + 1

    F = [[inf]*sum_energy for _ in range(n)]

    F[0][A[0]] = 0

    for i in range(1,n):
        for j in range(A[i], sum_energy):
            for k in range(i):
                if sum_energy > j + i - k - A[i]:
                    F[i][j] = min(F[k][max(j + i - k - A[i], 0)] + 1,F[i][j]) #cofam sie o i - k




    min_ = inf
    for i in range(sum_energy):
        if min_ > F[n-1][i]:
            min_ = F[n-1][i]

    return min_

A = [1,2,3,4,5]
B = [1,2,2,2,2,2]
C = [2,2,1,0,0]
D = [2,2,1,0,0,0]
E = [2,2,1,0,0,0,0]
F = [4,5,2,5,1,2,1,0]
print(frog(A))
print(frog(B))
print(frog(C))
print(frog(D))
print(frog(E))
print(frog(F))