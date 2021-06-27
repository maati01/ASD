from zad3testy import runtests
from zad3EK    import edmonds_karp
from math import inf

#tworze dwa super wierzchołki do sprawdzenia przepływu
#obliczam gdzie dystanse wynoszą >= d
#tworze krawedzie skierowane z 'B' do 'G'
#sprawdzam ile wynosi skojrzanie (w tym przypadku przepływ)

def floyd_warshall(G):
    n = len(G)

    P = [[None]*n for _ in range(n)] #poprzednik v na najkrótszej ścieżce z u do v,parents
    S = [[inf]*n for _ in range(n)] #macierz dł. najkrótszych ścieżek używających {v1,...,vt} jako wewnętrzne

    for i in range(n):
        S[i][i] = 0

    for i in range(n): #bezposrednie krawedzie jako minimalne sciezki wyjsciowe
        for j in range(n):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
                P[i][j] = i

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]

    return S

def BlueAndGreen(T, K, D):
    n = len(T)

    new_G = [[0]*(n+2) for _ in range(n+2)]

    for j in range(n):
        if K[j] == 'B': #krawędzie skierowowane z nowego wierzchołka do 'B'
            new_G[0][j+1] = 1
        else: #krawędzie skierowane z 'G' do drugiego nowego wierzchołka
            new_G[j+1][n+1] = 1

    S = floyd_warshall(T)

    for i in range(n):
        for j in range(n):
            if S[i][j] >= D and K[i] == 'B':
                new_G[i+1][j+1] = S[i][j]

    return edmonds_karp(new_G,0,n+1)

runtests( BlueAndGreen )