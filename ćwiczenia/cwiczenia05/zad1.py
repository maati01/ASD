# f(r,p) = {f(i - 1,p) , p<= P[i]
#          {min(f(i - 1,p),f(i-1,p - P[i] + W[i])) , p>= P[i]
# res = max(p | f(i,p) <= W)

def knapsack(W,P,MaxW): # złożoność O(n * sum_)
    n = len(W)
    sum_ = sum(P)
    w = sum(W)
    F = [[0] + [w+1] * sum_ for _ in range(n)]
    F[0][P[0]] = W[0]
    for i in range(1,n): # O(n)
        for p in range(sum_ + 1): #O(sum_)
            if p < P[i]:
                F[i][p] = F[i - 1][p]
            else:
                F[i][p] = min(F[i-1][p], F[i-1][p- P[i]] + W[i])
    for p in range(sum_, -1, -1):
        if F[n-1][p] != w + 1 and F[n-1][p] <= MaxW:
            return p, F
    return None,None

def getSolution(F,W,P,i,p):
    if p == 0:
        return []
    if i == 0:
        return [0]
    if F[i-1][p] == F[i][p]:
        return getSolution(F,W,P,i-1,p)
    return getSolution(F,W,P,i-1, p - P[i]) + [i]

P = [5,2,3,7,6,13]
W = [7,6,10,9,42,13]
n = len(W)
MaxW = 27
res, F = knapsack(W,P, MaxW)
if res is not None:
    print(res, getSolution(F,W,P,n-1,res))
else:
    print("Brak rozwiązania")
