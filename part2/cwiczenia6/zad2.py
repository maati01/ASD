#f(i) - największa wieża kończąca sie na i-tym
#f(i) = max(f(i),f(k) + 1) po k od 0 do i - 1

def klocki(T):
    n = len(T)
    F = [1]*n #wypełniam jedynkami bo to startowa długość wieży z jednym klockiem


    for i in range(n):
        for k in range(0,i):
            if T[i][0] >= T[k][0] and T[i][0] <= T[k][1] and  T[i][1] >= T[k][0] and T[i][1] <= T[k][1]: #sprawdzam czy moge polozyc i-ty na k-tym
                F[i] = max(F[i],F[k] + 1)

    print(F)
    return n - max(F)






T = [[1,2],[1,3],[1,2],[1,1],[1,2],[1,1],[0,1],[1,1],[1,2]]
print(klocki(T))