from math import inf


#dla grafów rzadkich lepsze jest rozwaizanie z wywoływaniem dijkstry dla kazdego wierzchołka i zapisywaniu w macierzy wszystkich odległości

def floyd_warshall(G):
    n = len(G)

    S = [[inf]*n for _ in range(n)] #macierz dł. najkrótszych ścieżek używających {v1,...,vt} jako wewnętrzne
    time = [[inf]*n for _ in range(n)] #na potrzeby zadania

    for i in range(n):
        S[i][i] = 0
        time[i][i] = 0

    for i in range(n): #bezposrednie krawedzie jako minimalne sciezki wyjsciowe
        for j in range(n):
            if G[i][j][0] != 0:
                time[i][j] = G[i][j][0]
            if G[i][j][1] != 0:
                S[i][j] = G[i][j][1]


    for t in range(n):
        for u in range(n):
            for v in range(n):
                if time[u][v] > time[u][t] + time[t][v] or (time[u][v] == time[u][t] + time[t][v] and S[u][v] > S[u][t] + S[t][v]): #modyfikacja,optymalizacja po czasie,a potem po drodze
                    S[u][v] = S[u][t] + S[t][v]
                    time[u][v] = time[u][t] + time[t][v]


    return time,S

def traffic_jam(G,Q):
    result = []
    time,D = floyd_warshall(G)

    for v in Q:
        result.append((time[v[0]][v[1]],D[v[0]][v[1]]))

    return result


#[(4, 14), (3, 4), (3, 5), (4, 2), (inf, inf)]
graph =[[(0,0),(1,3),(3,5),(0,0),(0,0),(2,1)], #krotyka(time,odległość)
        [(0,0),(0,0),(2,1),(0,0),(0,0),(1,1)],
        [(3,5),(0,0),(0,0),(1,10),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(2,1),(0,0),(0,0)],
        [(2,1),(1,1),(0,0),(0,0),(2,1),(0,0)]]
Q = [(0,3),(0,2),(2,0),(5,3),(3,2)]
print(traffic_jam(graph,Q))

#[(4, 15), (3, 21)]
graph =[[(0,0),(0,0),(3,5),(0,0),(0,0),(2,1)], #krotyka(time,odległość)
        [(0,0),(0,0),(2,1),(0,0),(0,0),(1,1)],
        [(3,5),(0,0),(0,0),(1,10),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(1,20),(0,0),(0,0)],
        [(2,1),(1,1),(0,0),(0,0),(2,1),(0,0)]]
Q = [(0,3),(5,3)]

print(traffic_jam(graph,Q))