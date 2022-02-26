#A[x,y] szachownica
#C(i,j) min koszt dojscia na pole i,j
#C[0,0] = A[0,0]
#C[i][0] = C[i-1][0] + A[i][0]
#C[0][j] = C[0][j - 1] + A[0][j]
#C[i][j] = min(C[i-1][j],C[i][j-1]) + A[i][j]

def chess_board(T):
    n = len(T)

    C = [[0]*n for _ in range(n)]

    for i in range(n):
        C[i][0] = C[i - 1][0] + T[i][0]
        C[0][i] = C[0][i - 1] + T[0][i]

    for i in range(1,n):
        for j in range(1,n):
            C[i][j] = min(C[i - 1][j], C[i][j - 1]) + T[i][j]

    return C[n-1][n-1]

T = [[1,1,1,4],[1,2,1,4],[1,2,1,4],[1,2,1,1]]
print(chess_board(T))