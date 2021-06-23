#f(i,t) = max wartość podziału a1,..,ai na t ciągów
#f(i,t) = min ( f(i - p, t - 1), suma od a(p + 1) do ai )

def better_sum(T,j,i):
    sum_ = 0
    for k in range(j,i):
        sum_ += T[k]

    return sum_

def sequences(T,k):
    n = len(T)
    F = [[0]*(k + 1) for _ in range(n)]

    val = 0
    for i in range(n):
        val += T[i]
        F[i][1] = val #jeden podciag jest suma wszystkich elementów


    min_val = 0

    for i in range(n):
        for j in range(2,k + 1):
            for p in range(i):
                val = min(F[i-p][j-1],better_sum(T,p + 1,i))
                if val > min_val:
                    min_val = val

            F[i][j] = min_val
            min_val = 0

    for i in range(n):
        for j in range(k+1):
            print(F[i][j], end = " ")
        print()


k = 3
#T = [5,6,4,3,12,1,6,7,8,7,7]
T = [1,2,3,5,6]
print(sequences(T,k))
