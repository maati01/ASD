from zad2testy import runtests
from math import inf


# f(i,j) - najmniejszy wynik tymczasowy od i do j
#f(i,j) = max{ abs(sum(i,j)), min{f(i,j-1),f(i+1,j)}}

def opt_sum(tab):
    n = len(tab)
    F = [[inf] * n for _ in range(n)]
    subsums = [0]*n
    temp = 0

    for i in range(n):
        F[i][i] = tab[i]
        temp += tab[i]
        subsums[i] = temp

    for i in range(n): #wypełniam pojedyńcze dodawania
        for j in range(i,n):
            if j + 1 < n:
                F[j][j + 1] = abs(F[j][j] + F[j+1][j+1])

    def f(i,j):
        if i + 1 == n or j - 1 == -1 or i >= j:
            return F[i][j]

        if F[i][j] == inf:
            x = f(i+1,j)
            y = f(i,j-1)
            val = subsums[j] - subsums[i] + tab[i]
            F[i][j] = max(abs(val),min(x,y))

        return F[i][j]


    f(0,n-1)

    return F[0][n-1]

runtests( opt_sum )
