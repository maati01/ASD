#zad z zestawu 5

def puotki(A,k):
    n = len(A)
    T = [ [-1]*n for i in range(k+1) ]

    def f(i, j, A):
        if T[i][j] >= 0: # TABLICA
            return T[i][j]
        if i == 0:
            T[i][j] = 0 # TABLICA
            return 0
        if i == 1:
            summ = 0
            for s in range(j + 1):
                summ += A[s]
            T[i][j] = summ # TABLICA
            return summ

        max_now = 0
        for p in range(j):
            summ = 0
            for l in range(p, j + 1):
                summ += A[l]
            fval = f(i - 1, p-1, A) # TU BYŁO    fval = f(i - 1, p, A)
            min_local = min(fval, summ)
            max_now = max(max_now, min_local)
        T[i][j] = max_now # TABLICA
        return max_now

    return f(k,n-1,A)

k = 3
#A = [5,6,4,3,12,1,6,7,8,7,7]
A = [1,2,3,5,6]
print(puotki(A,k))