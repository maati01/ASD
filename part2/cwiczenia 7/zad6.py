#dla nieparzystej ilosci elementów mediana
#dla parzystej jedna z liczb srodkowych

#dowód
# jezeli x bedzie nalezal do przedzialu (A[n//2-1], A[n//2+1]) to suma odleglosci
# elementow poza n//2-tym bedzie stala.
# dlatego, ze zmiana wartosci x na x +/- i, gdzie A[n//2-1] < x + i < A[n//2+1],
# skutkuje tym, ze dla wszystkich elementow < n//2: sum +/-= i oraz dla > n//2: sum -/+= i => nawzajem sie redukuja
# wracajac do elementu n//2-ego, abs(A[n//2] - x) osiaga min dla x = A[n//2]
# jezeli x bedzie nalezal do przedzialu spoza (A[n//2-1], A[n//2+1]) to
# suma jeszcze bardziej wzrosnie poniewaz trzeba bedzie doliczyc dystans na
# 'wracanie sie'
#tylko to jest dla nieparzystej ilosci elementow, dla parzystej trzeba by dopowiedziec
#ale dzialanie analogiczne

def sum_distance(A):
    n = len(A)
    sum1 = 0
    sum2 = 0
    if n % 2 != 0: return A[n//2]
    else:
        for i in range(n):
            sum1 = abs(A[i] - A[n//2 - 1])
            sum2 = abs(A[i] - A[n//2])

        if sum1 > sum2:
            return A[n//2]
        else:
            return A[n //2 - 1]

A = [1,2,100]
B = [1,2,50,100]
print(sum_distance(A))
print(sum_distance(B))