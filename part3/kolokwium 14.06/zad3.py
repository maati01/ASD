from zad3testy import runtests
from zad3EK    import edmonds_karp
from math import inf

#Mateusz Powęska
#tworze dwa super-wierzchołki, jeden ma połączenie tylko z 'B', a drugi tylko z 'G', krawedzie sa skierowane
#szukam maksymalnego przepływu z pierwszego do ostatniego wierzchołka
#dzieki temu mam pewność ze przejde przez B i G w przepływie
#dzieki zastosowaniu algorytmu edmondsa_karpa otrzymuje sieć resiudalną
#w sieci residualnej uruchamiam dijkstre z ostatniego do pierwszego wierzchołka,
#wracam po sciezce i sprawdzam czy zgadzaja sie warunki zadania
#jesli tak zwiekszam rezultat o jeden
#rozwiazanie ogranicza algorytm edmondsa karpka czyli O(E^2*V)

def minimum_distance(d,n,v,processed): #funkcja szuka minimalnego dystansu
    ind = None
    minimum = inf
    for i in range(n):
        if not processed[i] and d[i] != inf and minimum > d[i] and i != v:
            minimum = d[i]
            ind = i

    return ind


def dijkstra(G,v):
    n = len(G)
    d = [inf]*n
    d[v] = 0 #koncowy minimalny dystans
    parents = [None]*n
    processed = [False]*n #wierzchołki przetworzone

    while v is not None:
        if not processed[v]: #sprawdzam tylko nieprzetworzone wierzchołki, to poprawia wydajnosc
            for i in range(n):
                if G[v][i] != 0 and d[i] > d[v] + G[v][i]: #relaksacja
                    d[i] = d[v] + G[v][i]
                    parents[i] = v
            processed[v] = True

        v = minimum_distance(d,n,v,processed)

    return d,parents

def BlueAndGreen(T, K, D):
    n = len(T) + 2
    G = [[0]*n for _ in range(n)]
    result = 0

    for i in range(n-2):
        if K[i] == 'B':
            #G[i+1][0] = 1
            G[0][i+1] = 1
        elif K[i] == 'G':
            #G[n-1][i+1] = 1
            G[i+1][n-1] = 1

    for i in range(1,n-1):
        for j in range(1,n-1):
            G[i][j] = T[i-1][j-1]


    edmonds_karp(G,0,n-1) #edmonds potrzebny do sieci
    check = True
    while check:
        distance,parents = dijkstra(G,n-1)
        temp_distance = 0
        path = []
        temp = 0
        while parents[temp] != None:
            path.append(temp)
            G[parents[temp]][temp] = 0
            temp = parents[temp]

        G[n-1][temp] = 0
        path.append(temp)

        x = K[path[1]-1]
        k = len(path)
        for i in range(1,k): #wracanie po sciezce
            temp_distance += G[path[i-1]][i]
            if temp_distance <= D and x != K[path[i]-1]:
                result += 1
                break

        check = False

        for i in range(n):
            if G[n-1][i] != 0:
                check = True

    return result


runtests( BlueAndGreen )
