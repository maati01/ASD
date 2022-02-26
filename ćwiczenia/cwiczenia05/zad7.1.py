# f(i,j) = min(f(i-1,j),f(i,j-1)) + A[i][j]
# f(0,0) = A[0][0]
# F[i][0] = F[i-1][0] + A[i][0]
# F[0][i] = F[0][i-1] + A[0][i]

from math import inf


def chess_board(A):
    n = len(A)
    F = [[inf] * n for _ in range(n)]
    result = []

    F[0][0] = A[0][0]
    F[1][0] = A[0][0] + A[1][0]
    F[0][1] = A[0][0] + A[0][1]

    for i in range(1, n):  # wypelnienie pierwszego rzedu i kolumny
        F[i][0] = F[i - 1][0] + A[i][0]
        F[0][i] = F[0][i - 1] + A[0][i]

    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + A[i][j]

    i = n - 1
    j = n - 1
    while i != 0 or j != 0:
        result.append((i, j))
        if F[i - 1][j] < F[i][j - 1]:
            i = i - 1
            j = j
        else:
            i = i
            j = j - 1

    result.append((0, 0))

    return F[n - 1][n - 1], result[::-1]


T = [[1, 1, 1, 4], [1, 2, 1, 4], [1, 2, 1, 4], [1, 2, 1, 1]]
#T = [[-3, 2, 4], [-2, -1, 6], [5, 2, 1]]
print(chess_board(T))
