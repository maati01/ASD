#problem plecakowy

def getsolution(F,W,P,i,w):
    if i == 0:
        if w >= W[0]: return [0]
        return []

    if w >= W[i] and F[i][w] == F[i-1][w - W[i]] + P[i]:
        return getsolution(F,W,P,i - 1,w - W[i]) + [i]

    return getsolution(F,W,P,i - 1,w)

def knapsack(W,P,MaxW):
    n = len(W)
    F = [None]*n

    for i in range(n):
        F[i] = [0]*(MaxW + 1)

    for w in range(W[0],MaxW + 1):
        F[0][w] = P[0]

    for i in range(1,n):
        for w in range(1,MaxW + 1):
            F[i][w] = F[i-1][w]

            if w >= W[i]:
                F[i][w] = max(F[i][w],F[i-1][w-W[i]] + P[i])

    result = getsolution(F, W, P, n-1, MaxW)
    result1 = [0]*len(result)

    for i in range(len(result)):
        result1[i] += P[result[i]]

    return F[n-1][MaxW],result1

P = [10,8,4,5,3,7]
W = [4,5,12,9,1,13]
MaxW = 24
print(knapsack(W,P,MaxW))