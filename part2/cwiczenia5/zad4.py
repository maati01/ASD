#f(i)(j) = min koszt mnozenia macierzy T[i:j]
#wynik F[0][n]
#F[i][j] = min po k pd i do j ((costF[i][k],F[k+1][j])) + F[i][k] + F[k+1][j]
#zakładam że mam podane tylko wymiary macierzy
from math import inf


def matrix(T):
    n = len(T)
    F = [[inf]*n for _ in range(n)]

    for i in range(n):
        F[i][i] = 0


    for l in range(1,n): #algorytm z koremna
        for i in range(n - l):
            j = i + l
            for k in range(j):
                F[i][j] = min(F[i][j],F[i][k] + F[k+1][j] + T[i][0]*T[k][1]*T[j][1])


    return F[0][n-1]

T1 = [[10,100],[100,10],[10,1000]] #
T2 = [[2,3],[3,6],[6,4],[4,5]] #124
T3 = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]] #15125
T4 = [[10,100],[100,5],[5,50]]
print(matrix(T1))
print(matrix(T2))
print(matrix(T3))
print(matrix(T4))