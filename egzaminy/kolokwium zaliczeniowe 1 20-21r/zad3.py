from zad3testy import runtests
from math import inf


# DP
# f(i,j) - najmniejsza liczba tankowań na i-tej stacji mając j paliwa
# f(i, j) = min { f(i - 1, j + (T[i]-T[i - 1]) ,   f(i - 1, max(j - V[i], 0) + (T[i] - T[i - 1])) + 1 }
# j + (T[i] - T[i - 1]) <= q
# max(j - V[i], 0) + (T[i] - T[i - 1]) <= q
# patrzę na i-1 stację, sprawdzam czy miałem wystarczająco paliwa żeby dojechąc do i-tej
# sprawdzam ile tankowań będę miał jeśli zatankuje na i-tej
# minimalizuje te wartości
# zapisuje w polu path '1' jeśli tankowałem oraz z obecną wartość paliwa
# to pomaga w odtworzeniu wyniku
# funkcja find_the_best szuka miejsca gdzie ostatni raz tankowałem minimalną liczbę razy zeby dotrzec do l
# rozwiązanie odczytuje rekurencyjnie dzięki polu path

def find_the_best(F, T, l):
    n = len(F)
    q = len(F[0])
    refueling = inf
    fuel = -inf
    ind = None

    for i in range(n):
        for j in range(q):
            if F[i][j] < refueling and F[i][j] != inf and T[i] + j >= l:
                refueling = F[i][j]
                ind = i
                fuel = j

    return ind, fuel


def get_result(path, i, fuel):
    if i == 0:
        return [i]
    elif path[i][fuel][0]:
        return get_result(path, i - 1, path[i][fuel][1]) + [i]
    else:
        return get_result(path, i - 1, path[i][fuel][1])


def iamlate(T, V, q, l):
    n = len(T)
    F = [[inf] * (q + 1) for _ in range(n)]
    path = [[[-1, -1] for _ in range(q + 1)] for _ in range(n)]

    for i in range(min(V[0] + 1, q + 1)):
        F[0][i] = 1
        path[0][i][0] = 1

    for i in range(1, n):
        for j in range(q + 1):
            if j + (T[i] - T[i - 1]) <= q and F[i - 1][j + (T[i] - T[i - 1])] < F[i - 1][
                max(j - V[i], 0) + (T[i] - T[i - 1])] + 1:
                F[i][j] = F[i - 1][j + (T[i] - T[i - 1])]
                path[i][j] = [0, j + (T[i] - T[i - 1])]
            elif max(j - V[i], 0) + (T[i] - T[i - 1]) <= q:
                F[i][j] = F[i - 1][max(j - V[i], 0) + (T[i] - T[i - 1])] + 1
                path[i][j] = [1, max(j - V[i], 0) + (T[i] - T[i - 1])]

    i, fuel = find_the_best(F, T, l)

    if i is None:
        return []

    return get_result(path, i, fuel)


runtests(iamlate)
