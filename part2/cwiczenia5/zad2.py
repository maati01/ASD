# f(i,j) = f(i-1,j) or f(i-1,j-A[i-1])

def has_subset_of_sum_t(arr: list, t):
    n = len(arr)
    solution = [None] * n
    if t > sum(arr) or t == 0:
        return False
    for i in range(n):
        solution[i] = [False] * (t + 1)
        if arr[i] <= t:
            solution[i][arr[i]] = True
    for i in range(1, n):
        for k in range(t):
            if k != arr[i] and solution[i - 1][k]:
                solution[i][k] = True
                if arr[i] + k <= t:
                    solution[i][arr[i] + k] = True
    for i in range(n):
        if solution[i][t]:
            return True, solution
    return False

has_subset_of_sum_t([13, 7, 21, 42, 32, 44, 52], 51)