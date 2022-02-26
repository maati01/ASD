#f(i,l,r) = {1, pierwsze i samochodów można rozmieścić na promie tak, że zostaje l miejsca po lewo i r miejsca po prawo
#           {0m w p.p
#wynik: masz po n,g,d (g,d >= 0) { n|f(n,l,r) = 1}
#f(0,L,L) = 1
#f(i,g,d) = f(i-1,l + A[i],r) or f(i-1,l ,r + A[i])
#da sie zrobic z tablica dwuwymiarową i sumą
def prom(A,L):
    n = len(A)
    F = [[[0 for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]
    last = 0
    left = []
    right = []
    last1 = 0
    last2 = 0

    if L - A[0] >= 0: #pierwszy samochód
        F[0][L - A[0]][L] = 1
        F[0][L][L - A[0]] = 1

    else:
        return 0

    for i in range(1,n):
        for l in range(L + 1):
            for r in range(L + 1):
                if l + A[i] <= L:
                    F[i][l][r] = F[i - 1][l + A[i]][r]
                if r + A[i] <= L:
                    F[i][l][r] = F[i - 1][l][r + A[i]] or F[i][l][r]

                if F[i][l][r] == 1:
                    last = i #ilosc samochodów
                    last1 = l
                    last2 = r

    if last == 0:
        left.append(A[0])
        return last + 1,left


    for i in range(last,-1,-1): #odtwarzanie rozwiazania jest problem
        if last1 + A[i] <= L and F[i][last1][last2] == 1: #jesli samochód poszedł na lewo
            left.append(A[i])
            last1 += A[i]
        else:
            right.append(A[i])
            last2 += A[i]


    return last + 1,left,right


#A = [1,3,2,4,1,3,2,4,6]
A = [1,2,3,6]
#A = [2,1,2,3]

print(prom(A,6))