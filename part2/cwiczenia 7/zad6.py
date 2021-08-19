#z jakiegoś powodu to mediana XD

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