# F[i][j] - najdluzszy wspolny podciag do i dla A oraz j dla B
# f(i,j) = { F[i][j] = F[i-1][j-1] + 1 , if A[i] == B[j]
#          { F[i][j] = max(F[i-1][j],F[i][j-1])

def longest(A,B):
    n = len(A) + 1
    k = len(B) + 1
    result = []

    F = [[0] * k for _ in range(n)]

    for i in range(1,n):
        for j in range(1,k):
            if(A[i-1] == B[j-1]): #roznica w indeksach dla F i A/B
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])

    temp = F[n-1][k-1]

    n -= 1
    k -= 1
    while n >= 0: #odczytanie rozwiazania (moga byc bledy)
        if(F[n][k] > max(F[n-1][k-1],F[n][k-1],F[n-1][k])):
            result.append(A[n-1])
            k -= 1
            n -= 1
        elif k > 1 and F[n][k] == F[n][k-1]:
            k -= 1
        else:
            n -= 1



    print(result[::-1])

    return temp

#A = 'DAMIAN'
#B = 'XDITN'
#A = [1,7,3,2]
#B = [7,2,4,2,3]
#A = 'Mati'
#B = 'Mati'
#A = 'abcdaf'
#B = 'acbcf'
#A = [4,2,5,8,7,5]
#B = [2,4,5,5,7,8]
A = [3,1,2,3,4] #tutaj był jakis problem
B = [1,2,3,3,4]

print(longest(A,B))