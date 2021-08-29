from zad1testy import runtests
from math import inf
from queue import PriorityQueue

#dijkstra z wielokrotnymi wierzchołkami
#wierzchołki mówią ile mam obecnie paliwa oraz najkrótszy dystans z tym paliwem

def minimum_distance(d, n, v, processed, tank):  # funkcja szuka minimalnego dystansu
    ind = None
    ind1 = None
    minimum = inf
    for i in range(n):
        for j in range(tank + 1):
            if not processed[i][j] and d[i][j] != inf and minimum > d[i][j] and i != v:
                minimum = d[i][j]
                ind = i
                ind1 = j

    return ind, ind1  # nowy wierzchołek i ilośc paliwa


def dijkstra(G, P, tank, v):
    n = len(G)
    d = [[inf] * (tank + 1) for _ in range(n)]
    d[v][tank] = 0  # koncowy minimalny dystans
    parents = [[(None, None)] * (tank + 1) for _ in range(n)]
    processed = [[False] * (tank + 1) for _ in range(n)]  # wierzchołki przetworzone
    curr_fuel = tank
    next_fuel = 0
    fuel = [0] * n
    Q = PriorityQueue()
    Q.put((0, v, curr_fuel))

    for i in range(len(P)):
        fuel[P[i]] = tank

    while not Q.empty():
        _, v, curr_fuel = Q.get()
        if not processed[v][curr_fuel]:  # sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if fuel[i] != 0 and G[v][i] != -1:  # paliwo dla wierzchołka i
                    next_fuel = tank
                elif fuel[i] == 0 and G[v][i] != -1:
                    next_fuel = curr_fuel - G[v][i]

                if G[v][i] != -1 and curr_fuel >= G[v][i] and d[i][next_fuel] > d[v][curr_fuel] + G[v][i]:  # relaksacja
                    d[i][next_fuel] = d[v][curr_fuel] + G[v][i]
                    parents[i][next_fuel] = (v, curr_fuel)
                    Q.put((d[i][next_fuel], i, next_fuel))

        processed[v][curr_fuel] = True

    return parents, d


def get_result(parents, x, y, fuel):
    if y == x:
        return [x]
    else:
        return get_result(parents, x, parents[y][fuel][0], parents[y][fuel][1]) + [y]


def jak_dojade(G, P, n, a, b):
    parents, d = dijkstra(G, P, n, a)

    fuel = n
    temp_min = inf
    for i in range(len(d[b])):  # szukam najlepszej sciezki majac i paliwa
        if d[b][i] < temp_min:
            temp_min = d[b][i]
            fuel = i

    if parents[b][fuel][0] is None:
        return None
    else:
        return get_result(parents, a, b, fuel)


runtests(jak_dojade)
