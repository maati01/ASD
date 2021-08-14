# f(i,j,k) - maksymalna wartość do itego przedmiotu zajmujac j wagi i k wysokości
# f(i,j,k) = max(F[i][j][k], F[i][j - w[i]][k - h[i]] + v[i])

def get_solution(F, j, k, v, w, h, i):
    if i == 0:
        if j >= w[0] and k >= h[0]:
            return [0]
        else:
            return []

    if j >= w[i] and k >= h[i] and F[i][j][k] == F[i - 1][j - w[i]][k - h[i]] + v[i]:
        return get_solution(F, j - w[i], k - h[i], v, w, h, i - 1) + [i]
    else:
        return get_solution(F, j, k, v, w, h, i - 1)


def knapsack_3_parameters(W, H, v, w, h):
    n = len(v)

    F = [[[0] * (H + 1) for _ in range(W + 1)] for _ in range(n)]

    F[0][w[0]][h[0]] = v[0]

    for i in range(1, n):
        for j in range(W + 1):
            for k in range(H + 1):
                F[i][j][k] = F[i - 1][j][k]
                if j >= w[i] and k >= h[i]:
                    F[i][j][k] = max(F[i][j][k], F[i - 1][j - w[i]][k - h[i]] + v[i])

    result = 0
    for i in range(W + 1):
        for j in range(H + 1):
            if F[n - 1][i][j] > result:
                result = F[n - 1][i][j]

    arr = get_solution(F, W, H, v, w, h, n - 1)

    return result, arr


v = [1, 2, 4, 1, 4]
w = [2, 3, 2, 4, 1]
h = [1, 2, 3, 1, 2]
W = 5
H = 7
print(knapsack_3_parameters(W, H, v, w, h)) #(9, [0, 2, 4])
W = 6
print(knapsack_3_parameters(W, H, v, w, h)) #(10, [1, 2, 4])

v = [5, 1, 100]
w = [5, 5, 6]
h = [5, 6, 10]
W = 10
H = 10
print(knapsack_3_parameters(W, H, v, w, h)) #(100, [2])

v = [10, 10, 14, 6, 12, 20, 5]
w = [15, 7, 8, 4, 1, 2, 5]
h = [15, 3, 6, 5, 15, 19, 2]
W = 24
H = 30
print(knapsack_3_parameters(W, H, v, w, h)) #(49, [1, 2, 5, 6])