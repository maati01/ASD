from zad2testy import runtests
from math import inf


# DP
# f(v,j) - najlepsze poddrzewo zaczynające się w v mające j krawędzi
# schodzę rekurencyjnie do liści, wstawiając w pole X [0,-inf,-inf,-inf,-inf...]
# wracajać rekurencyjnie w wierzchołku obliczam najlepsze poddrzewo
# f(v,j) = max(v.left.X[j - l] + v.right.X[l - 2] + v.rightval + v.leftval,v.X[j]) dla l >= 2
# jeśli l == j to biorę całe prawe poddrzewo plus prawą krawędź
# jeśli l == 0 to biorę całe lewe poddrzewo plus lewą krawędź
# O(v*k^2)

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def valuableTree(T, k):
    def f(v):
        if v is None:
            return
        v.X = [-inf] * (k + 1)
        v.X[0] = 0

        f(v.left)
        f(v.right)

        for j in range(1, k + 1):
            for l in range(j + 1):
                if l == 0 and v.left is not None:
                    v.X[j] = max(v.left.X[j - 1] + v.leftval, v.X[j])
                if l == j and v.right is not None:
                    v.X[j] = max(v.right.X[j - 1] + v.rightval, v.X[j])
                if v.right is not None and v.left is not None and l >= 2:
                    v.X[j] = max(v.left.X[j - l] + v.right.X[l - 2] + v.rightval + v.leftval, v.X[j])

    f(T)

    result = -inf

    def check_result(T, k):
        nonlocal result
        if T is None:
            return

        check_result(T.left, k)
        check_result(T.right, k)

        if T.X[k] > result:
            result = T.X[k]

    check_result(T, k)

    return result


runtests(valuableTree)
