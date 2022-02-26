#f(i) = min liczba monet do wydania i
#f(i) = min f(i - mj) + 1

from math import inf

def coins(M,x):
    n = len(M)
    result = [0]*(x + 1) #ilosc poszczególnych monet
    F = [inf]*(x + 1)
    F[0] = 0

    for i in range(1,x + 1):
        for j in range(n):
            if  i - M[j] >= 0 and F[i] > F[i - M[j]] + 1:
                F[i] = F[i - M[j]] + 1
                result[i] = M[j]
            if i - M[j] == i - 1 and F[i] == inf:
                F[i] = F[i - 1] + 1
                result[i] = M[j]


    if(F[x] == inf):
        return False

    print("coins:",end =" ")

    i = x
    while(i != 0):
        if result[i] != 0:
            print(result[i],end =" ")
            i -= result[i]

    print()

    return F[x]


M = [1,5,8,100]
x = 4001

print(coins(M,x))


