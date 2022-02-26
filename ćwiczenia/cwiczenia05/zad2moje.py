#f(i,j)  = f(i-1,j) v f(i-1,j - A[i])

def has_subset_of_sum_t(A,T):
    n = len(A)

    F = [[0]*(T + 1) for _ in range(n)]

    for i in range(n):
        F[i][0] = 1

    if T >= A[0]:
        F[0][A[0]] = 1

    for i in range(1, n):
        for j in range(T + 1):
            if A[i] > j:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = F[i-1][j] or F[i-1][j - A[i]]

    for i in range(n):
        if F[i][T] == 1:
            return True

    return False


print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 51))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 8))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 20))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 22))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52, 4], 22))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52, 4], 4))
print(has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52, 4], 100))