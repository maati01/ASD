# f(i,j) = max(min(f(i - p,j - 1),sum(i - p,i))), p (1, i + 1)
# min value do itego indeksu na j podciągów
#sprawdzam czy mogę stworzyć przedział który poprawi mi minimalny

def maximin(A, k):
    n = len(A)
    sum_to_i = [0] * n
    F = [[0] * (k + 1) for _ in range(n)]

    temp = 0
    for i in range(n):
        temp += A[i]
        sum_to_i[i] += temp
        F[i][1] = temp

    for i in range(1,n):
        for j in range(2, k + 1):
            if i + 1 >= j:
                for p in range(1, i + 1):
                    temp_val = sum_to_i[i] - sum_to_i[i - p]
                    temp_min = min(F[i - p][j - 1], temp_val)
                    if temp_min > F[i][j]:
                        F[i][j] = temp_min

    return F[n-1][k]

print(maximin([1, 2, 3, 5, 6], 3)) #5
print(maximin([5, 6, 4, 3, 12, 1, 6, 7, 8, 7, 7], 3)) #18
print(maximin([1, 2, 3, 5, 1, 6], 3)) #6
print(maximin([1, 2, 3, 5, 1, 6], 4)) #3
print(maximin([1, 2, 3, 5, 1, 6], 5)) #1
print(maximin([1, 2, 3, 5, 1, 6], 6)) #1
print(maximin([16, 3, 3, 3, 0, 1, 2, 3, 5, 1, 6,1000], 6)) #6