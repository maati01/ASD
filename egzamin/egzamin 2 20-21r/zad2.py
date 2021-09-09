from zad2testy import runtests, Node
from math import inf


# liczę sume poddrzew rekurencyjnie
# sprawdzam czy jeśli usunę itą krawędź róźnica dwóch powstałych drzew będzie mniejsza od obecnej
# sprawdzam to rekurencyjnie z obecną róźnicą która jest globalna
# jesli tak to nadpisuje różnicę i zapamiętuje indeks krawędzi
# O(n)

def calculate_sums(T):  # funkcja oblicza sume poddrzewa w T
    val = 0
    if len(T.edges) == 0:
        return 0

    for i in range(len(T.edges)):
        val += calculate_sums(T.edges[i])
        val += T.weights[i]

    T.sum = val

    return val


def balance(T):
    calculate_sums(T)

    result = inf
    ind = 1
    global_sum = T.sum

    def find_the_best_edge(T):
        nonlocal result, ind
        if len(T.edges) == 0:
            return

        for i in range(len(T.edges)):
            if abs(T.edges[i].sum - (global_sum - T.weights[i] - T.edges[i].sum)) < result:
                result = abs(T.edges[i].sum - (global_sum - T.weights[i] - T.edges[i].sum))
                ind = T.ids[i]

            find_the_best_edge(T.edges[i])
        return

    find_the_best_edge(T)
    return ind


runtests(balance)
