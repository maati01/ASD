#f(i,j) = min liczba skoków zeby dotrzeć do i-tego pola
#         i mieć j jednostek energii(już po zjedzeniu A[i])
#Rozwiązanie: min f(n-1,j)ypyy
#f(i,j) = min f(k, j - k - A[i]) + 1
#f(i,-j) = inf

from math import inf

def frog(A):
    n = len(A)
    F = [[inf]*n for _ in range(n)]
    for i in range(A[0] + 1):
        F[0][i] = 0

    for i in range(1,n):
        for j in range(n):
            for k in range(1,i+1): #rozwiązanie z bit algo
                if j + k - A[i] < n:
                    F[i][j] = min(F[i][j], F[i - k][max(j + k - A[i],0)] + 1)  #max zabezpiecza nas przed <0

    for i in range(n):
        print(F[i])


    return min(F[n-1])



A = [1,2,3,4,5]
#A = [1,2,2,2,2,2]
#A = [2,2,1,0,0,0]
#A = [4,5,2,5,1,2,1,0]
print(frog(A))