#lekko zmodyfikowany bellman ford
#sortuje po wartościach krawedzie
#dobieram sciezke od najwiekszej
#jesli pasuje do poprzedniego wierzchołka to kontynuje
#jesli nie to pomijam
#to mi gwarantuje ze zawsze dobiore od najwiekszej do najmniejszej
from math import inf

def get_result(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_result(parents,x,parents[y]) + [y]

def decreasing_edges(G,x,y):
    n = len(G)
    G.sort(key=lambda x: x[2], reverse=True)
    max_v = -inf

    for i in range(n):
        max_v = max(max_v,G[i][0],G[i][1])

    parents = [None]*(max_v + 1)
    visited = [0]*(max_v + 1)
    prev_e = [None]*(max_v + 1)
    visited[x] = 1

    for i in range(n):
        v1 = G[i][0]
        v2 = G[i][1]
        if G[i][2] != prev_e[v1] and not visited[v2]: #jesli chcemy minimalny dystans wystarczy zrelaksować wierzchołek
            prev_e[v2] = G[i][2]
            parents[v2] = v1
            visited[v2] = 1

    if parents[y] is None:
        return False
    else:
        return get_result(parents,x,y)


G = [[0,1,1],[0,3,3],[1,0,1],[1,2,1],[2,1,1],[2,4,1],[3,0,3],[3,4,2],[4,2,1],[4,3,2]] #(v1,v2,waga)
print(decreasing_edges(G,0,2)) #[0,3,4,2]
G = [[0,1,1],[0,3,3],[1,0,1],[1,2,1],[2,1,1],[2,4,1],[3,0,3],[3,4,1],[4,2,1],[4,3,1]]
print(decreasing_edges(G,0,2)) #False
G = [[0,1,1],[0,3,3],[1,0,1],[1,2,1],[2,1,1],[2,4,1],[3,0,3],[3,4,2],[4,2,1],[4,3,2]]
print(decreasing_edges(G,3,2)) #[3,4,2]