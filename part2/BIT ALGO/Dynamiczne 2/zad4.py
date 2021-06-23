def pascal(T,k,P):
    n = len(T)
    F = [[0]*(k+1) for _ in range(n)]

    for i in range(n):
        temp = 0
        for j in range(k,-1,-1):
            temp += T[i][j]
            F[i][k - j] = temp
    


    print(F)



T = [[1,2,3],[1,2,3],[1,2,3],[1,1,1]]
k = 2
P = 4
pascal(T,k,P)