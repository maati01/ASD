from zad1testy import runtests
from math import inf

#DP
#mapuje i sortuje po współrzędnych
#F[i][j] - największa ilość studentów do i-tego akademika mając j kosztu
#F[i][j] = max(F[i][j],F[k][j],F[k][j - cost[i]] + students(i)), gdzie k od 0 do i
#k-ty akademik nie może nachodzić na i-ty akademik
#do odtworzenia wyniku w polach parents zapisuje z jakiego wierzchołka przyszedłem i z jakim kosztem
#funkcja find_max gwarantuje że odtworzę wynik z największą ilością studentów i najmniejszym kosztem
#rozwiązanie odtwarzam rekurencyjnie za pomocą tablicy parents
#O(p*n^2)

def map_and_check_prev(T):
    n = len(T)

    for i in range(n):
        T[i] = [T[i][0], T[i][1], T[i][2], T[i][3], i]  # (h, a, b, w, i, prev)

    T.sort(key=lambda x: x[2])
    T.sort(key=lambda x: x[1])

    return T


def students(T, i):
    return T[i][0] * (T[i][2] - T[i][1])


def get_result(parents, dormitories, i, cost):
    if parents[i][cost] == [-1, -1]:
        return [dormitories[i][4]]

    else:
        return get_result(parents, dormitories, parents[i][cost][0], parents[i][cost][1]) + [dormitories[i][4]]


def find_max(T):
    n = len(T)
    m = len(T[0])
    _max = -inf
    ind = inf
    cost = None
    for i in range(n):
        for j in range(m):
            if T[i][j] > _max:
                _max = T[i][j]
                ind = i
                cost = j
            if T[i][j] == _max and j < cost:
                ind = i
                cost = j

    return ind, cost


def select_buildings(T, p):
    n = len(T)
    F = [[0] * p for _ in range(n)]
    parents = [[[-1, -1] for _ in range(p)] for _ in range(n)]
    dormitories = map_and_check_prev(T)

    for i in range(n):
        F[i][dormitories[i][3]] = students(dormitories, i)
    for i in range(1, n):
        for j in range(p):
            for k in range(i):

                if F[k][j] > F[i][j]:
                    F[i][j] = F[k][j]

                if dormitories[i][1] > dormitories[k][2] and j - dormitories[i][3] >= 0:
                    if F[i][j] < F[k][j - dormitories[i][3]] + students(dormitories, i):
                        F[i][j] = F[k][j - dormitories[i][3]] + students(dormitories, i)
                        parents[i][j] = [k, j - dormitories[i][3]]

    ind, cost = find_max(F)

    return sorted(get_result(parents, dormitories, ind, cost))


runtests(select_buildings)
