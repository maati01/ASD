from zad1testy import runtests

#sortuje pierwsze po y, potem po x
#biore najwiekszy punkt i pomijam punkty dopóki je dominuje
#wybieram następny i powtarzam
#O(nlogn)

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

    for i in range(n): #tworze krotke zeby zapamietac indeks przed posortowaniem
        P[i] = P[i][0],P[i][1],i

    P = quick_sort(P,1)
    P = quick_sort(P,0)
    result = []

    i = 0
    potential = P[0]

    while i < n:
        if potential[0] > P[i][0] or potential[1] > P[i][1]:
            result.append(potential[2])
            potential = P[i]

        i += 1
    result.append(potential[2])

    return result

runtests( dominance )