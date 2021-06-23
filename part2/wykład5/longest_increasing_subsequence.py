def printLIS(A,P,i):
    if P[i] >= 0:
        printLIS(A,P,P[i])
    print(A[i],end = " ")

def lis(A):
    n = len(A)
    F = [1]*n
    P = [-1]*n #tablica która trzyma kontynuacje ciagu rosnacego
    for i in range(1,n): #O(n^2)
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1
                P[i] = j

    index_max = max(range(len(F)),key = F.__getitem__) #właność pythona z wykładu
    printLIS(A,P,index_max)

    return (max(F),F,P)

#lis([3,1,5,7,2,4,9,3,18,3])
lis([2,1,4,3])
