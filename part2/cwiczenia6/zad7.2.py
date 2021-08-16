from math import inf

#to samo co 7.1 tylko szukam min kosztu

def sticking_with_costs(T, a, b):
    n = len(T)
    F = [[inf] * (b - a + 1) for _ in range(n)]
    T.sort(key=lambda x: x[0])
    last = None

    for i in range(n):
        if T[i][0] == a:
            last = i
            F[i][T[i][1] - T[i][0]] = T[i][2]

    if last is None:
        return inf

    for i in range(last, n):
        for j in range(b - a + 1):
            for k in range(i):
                if j + a == T[i][1]:
                    F[i][j] = min(F[i][j],F[k][j - (T[i][1] - T[i][0])] + T[i][2],F[i][j])


    result = inf

    for i in range(n):
        if F[i][b - a] < result:
            result = F[i][b - a]

    return result


T = [[4, 6,1], [7, 9,2], [3, 4,1], [6, 8,2], [9, 10,5], [4, 7,3], [8, 10,1]]
a = 3
b = 10
print(sticking_with_costs(T, a, b)) #5
a = 2
b = 10
print(sticking_with_costs(T, a, b)) #inf
T = [[4, 6, 1], [7, 9, 2], [3, 4, 1], [6, 8, 2], [9, 10, 5], [4, 7, 3], [8, 10, 1]]
a = 3
b = 9
print(sticking_with_costs(T, a, b)) #6
T = [[4, 6, 1], [7, 9, 2], [3, 4, 1], [6, 8, 2], [9, 10, 5], [4, 7, 3], [8, 10, 100]]
a = 3
b = 10
print(sticking_with_costs(T, a, b)) #11
A = [[0, 3,0], [3, 7,999], [0, 1,10], [1, 2,20], [2, 7,30], [4, 3,4], [-2, 0,7]]
a = 0
b = 7
print(sticking_with_costs(A, a, b)) #60