from math import inf

#rozmnażam wierzchołki na D opcji
#zaaczynam z pełnym bakiem
#tworze krawedzie miedzy mozliwymi polączeniami stanu baku
#O(v^2 * d^2) ?
#można lepiej, zrobione w 7.1

def minimum_distance(d, n, v, processed,D):  # funkcja szuka minimalnego dystansu
    ind = None
    last_D = None
    minimum = inf
    for i in range(n):
        for j in range(D):
            if not processed[i][j] and d[i][j] != inf and minimum > d[i][j] and i != v:
                minimum = d[i][j]
                ind = i
                last_D = j
    return ind, last_D


def dijkstra(G, v, D, stations):
    n = len(G)
    d = [[inf] * (D + 1) for _ in range(n)]
    parents = [[None] * (D + 1) for _ in range(n)] #w parentach trzymam ostatni wierzchołek i jego aktualny stan paliwa
    processed = [[False] * (D + 1) for _ in range(n)]
    d[v][D] = 0 #zaaczynam z pelnym
    last_D = D
    #d[v][0] = 0 #zaczynam z pustym
    #last_D = 0

    while v is not None:
        if processed[v][last_D] is not processed:
            for i in range(n):
                if v != i and D >= G[v][i] > 0 :
                    val1 = last_D + (max(0,D - last_D)) - G[v][i] #maksymalna pojemnosc baku z jaka moge dojechac do wierzchołka i
                    val2 = last_D - G[v][i] #maksymalna pojemnosc baku z jaka moge dojechac do wierzchołka i
                    for j in range(max(val2,0), val1 + 1):
                        if d[i][j] > d[v][last_D] + stations[v]*(max(0,j + G[v][i] - last_D)): #relaksuje uwzględniając ile paliwa zatankuje
                            d[i][j] = d[v][last_D] + stations[v]*(max(0,j + G[v][i] - last_D)) #niekoniecznie musze tankowac
                            parents[i][j] = (v,last_D)
            processed[v][last_D] = True

        v,last_D = minimum_distance(d, n, v, processed,D)

    return d, parents

def get_result(d,parents,A,B):
    path = []
    n = len(parents[B])
    min_v = inf
    min_ind = 0
    for i in range(n):
        if parents[B][i] is not None and d[B][i] < min_v:
            min_v = d[B][i]
            min_ind = i

    while B != A:
        path.append(B)
        B, min_ind = parents[B][min_ind]

    path.append(A)

    return path[::-1]


def fuel_stations(G,A,B,D,stations):
    d, parents = dijkstra(G,A,D,stations)

    if d[B] == inf:
        return False
    else:
        return get_result(d,parents,A,B), min(d[B])


stations = [2,1,1,10]
G = [[0,2,0,2],
     [2,0,1,0],
     [0,1,0,1],
     [2,0,1,0]]
A = 0
B = 2
D = 2
print(fuel_stations(G,A,B,D,stations)) #[0, 1, 2]

stations = [3, 6, 4, 2, 1, 3, 2, 0]
G = [[0, 5, 6, 0, 1, 0, 0, 0],
[5, 0, 2, 1, 3, 0, 8, 0],
[6, 2, 0, 3, 0, 4, 0, 0],
[0, 1, 3, 0, 0, 3, 0, 0],
[1, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 4, 3, 0, 0, 3, 0],
[0, 8, 0, 0, 0, 3, 0, 3],
[0, 0, 0, 0, 0, 0, 3, 0]]
A = 0
B = 7
D = 10
print(fuel_stations(G,A,B,D,stations))