from math import inf
# F[i][j] - min liczba odcinkow, ktore trzeba skleic zeby powstal odcinek od i do j
# F[i][j] = min(F[i][k] + F[k][j], F[i][j])
# zadanie podobne do nawiasowania macierzy

def map_to_array(T):
    n = len(T)
    A = []
    for i in range(len(T)):
        A.append(T[i][0])
        A.append(T[i][1])

    A.sort()
    B = [A[0]]

    for i in range(1,2*n):
        if A[i] != A[i-1]:
            B.append(A[i])

    return B


def max_sticking(T, cnt):
    T.sort(key=lambda x: x[0])
    A = map_to_array(T)
    n = len(A)
    F = [[inf]*n for _ in range(n)]

    m = len(T)
    ind1 = 0
    ind2 = 0
    for i in range(m):
        for j in range(n):
            if T[i][0] == A[j]:
                ind1 = j
        for j in range(n):
            if T[i][1] == A[j]:
                ind2 = j

        #F[i][i] = 0
        F[ind1][ind2] = 1

    for i in range(n):
        F[i][i] = 0


    for i in range(n):
        for j in range(i + 1,n):
            for k in range(i,j):
                F[i][j] = min(F[i][k] + F[k][j], F[i][j])

    result = None, None, 0
    for i in range(n):
        for j in range(n):
            if F[i][j] <= cnt and A[j] - A[i] > result[2]:
                result = (A[i],A[j],A[j] - A[i])

    return result


A = [(0, 3), (3, 7), (3, 4), (-2, 0)]; k = 3 #(-2, 7, 9)
print(max_sticking(A,k))

A = [(0, 3), (3, 9), (0, 5), (5, 8), (8, 14), (3, 4), (-2, 0)]; k = 4 #(-2, 14, 16)
print(max_sticking(A,k))

A = [(0, 3), (3, 9), (0, 5), (5, 8), (8, 14), (3, 4), (-2, 0),(-3,0)]; k = 4 #(-3, 14, 17)
print(max_sticking(A,k))

A = [(0, 3), (3, 9), (0, 5), (5, 8), (8, 14), (3, 4), (-2, 0),(-4,-2),(-3,0)]; k = 5 #(-4, 14, 18)
print(max_sticking(A,k))

A = [(1,2),(1,3),(1,4),(2,6),(3,6),(2,3),(3,6)]; k = 3 #(1, 6, 5)
print(max_sticking(A,k))