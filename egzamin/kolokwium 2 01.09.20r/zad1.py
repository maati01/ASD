from zad1testy import runtests

def quick_sort(A,ind):
    p = 0
    r = len(A)-1
    def sub_quick_sort(A,p,r):
        if p < r:
            q = partation(A,p,r)
            sub_quick_sort(A,p,q-1)
            sub_quick_sort(A,p+1,r)

    def partation(A,p,r):
        x = A[r][ind]
        i = p-1
        for j in range(p,r):
            if A[j][ind] <= x:
                i += 1
                A[i],A[j] = A[j],A[i]

        A[i+1],A[r] = A[r],A[i+1]
        return i+1

    sub_quick_sort(A,p,r)
    return A

def dominance(P):
    n = len(P)
    S = []
    for i in range(n):
        x,y = P[i][0],P[i][1]
        P[i] = (x,y,i)

    P = quick_sort(P,1) #po y
    P = quick_sort(P,0) #po x

    temp = P[0][1]
    S.append(P[0][2])
    for i in range(1,n):
        if P[i][1] < temp:
            temp = P[i][1]
            S.append(P[i][2])


    return S

runtests( dominance )