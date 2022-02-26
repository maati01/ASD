#wybieram od najwiekszych mozliwych ładunków
#dowód jest przez przesuwanie binarne
#głównie chodzi o to że to najkorzystniejsza opcja brać największy możliwy ale tylko dlatego że to potęgi dwójek

def landing(A,K):
    n = len(A)
    i = 0
    result = []
    cnt = 0
    A.sort(reverse=True)

    while i < n:
        if A[i] + cnt <= K:
            result.append(A[i])
            cnt += A[i]

        i += 1

    return result, cnt

A = [2,2,4,8,1,8,16]
K = 27
print(landing(A,K)) #([16, 8, 2, 1], 27)

A = [2,2,4,8,1,8,16]
K = 26
print(landing(A,K)) #([16, 8, 2], 26)

A = [2,2,4,8,8,16]
K = 27
print(landing(A,K)) #([16, 8, 2], 26)

A = [2,2,4,8,8,16]
K = 25
print(landing(A,K)) #([16, 8], 24)