#f(i) - najwiekszy zysk do i-tego drzewa
#f(i) = max(f(i-1),f(i-2) + ci)
def black_forest(c):
    n = len(c)
    F = [0]*n
    F[0] = c[0]
    F[1] = max(c[0],c[1])
    for i in range(2,n):
        F[i] = max(F[i-1],F[i-2] + c[i])

    return F[n-1]

c = [12,14,1,1,2,102,100]
print(black_forest(c))