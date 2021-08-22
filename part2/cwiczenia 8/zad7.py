#używam wierzchołka tylko z wartością 1
#jeśli ma większą wartość to zmniejszam o 1 i wrzucam go ponownie do kolejki
#to sprawia że priorytet mają pola o najmniejszej wartości
#odległość dodaje gdy tymczasowa wartosc bedzie rowna 1
from queue import Queue
from math import inf

def get_solution(parents,v,w):
    if w is None:
        return []
    else:
        return get_solution(parents,v,parents[w[0]][w[1]]) + [(w[0],w[1])]

def chess_board(G):
    directions = [(-1, -1), (0, -1), (1, -1),(-1, 0), (1, 0),(-1, 1), (0, 1), (1, 1)]
    n = len(G)
    Q = Queue()
    visited = [[False]*n for _ in range(n)]
    d = [[inf]*n for _ in range(n)]
    parents = [[None]*n for _ in range(n)]

    d[0][0] = G[0][0]
    Q.put((G[0][0],0,0)) #(aktualna waga krawedzi, wspolrzedne)
    visited[0][0] = True

    while not Q.empty():
        val,x,y = Q.get()
        if val > 1:
            val -= 1
            Q.put((val, x, y))
            continue
        for i in range(8):
            v = (x + directions[i][0],y + directions[i][1])
            if 0 <= v[0] < n and 0 <= v[1] < n and not visited[v[0]][v[1]]:
                visited[v[0]][v[1]] = True
                d[v[0]][v[1]] = d[x][y] + G[v[0]][v[1]]
                parents[v[0]][v[1]] = (x,y)
                Q.put((G[v[0]][v[1]],v[0],v[1]))

    return get_solution(parents,(0,0),(n-1,n-1)), d[n-1][n-1]

# [(0, 0), (0, 1), (1, 2), (2, 1), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
# 7
A = [[0, 1, 1, 5, 5],
     [5, 5, 1, 5, 5],
     [1, 1, 1, 5, 5],
     [1, 5, 5, 5, 5],
     [1, 1, 1, 1, 0]]


print(chess_board(A))
# [(0, 0), (0, 1), (0, 2), (1, 3), (2, 2), (3, 1), (4, 2), (4, 3), (4, 4)]
# 7
A = [[0, 1, 1, 1, 1],
     [5, 5, 5, 1, 5],
     [5, 5, 1, 5, 5],
     [5, 1, 5, 5, 5],
     [1, 1, 1, 1, 0]]
print(chess_board(A))
# [(0, 0), (0, 1), (1, 2), (2, 2)]
# 4
A = [[0, 3, 2],
     [1, 5, 1],
     [2, 5, 0]]
print(chess_board(A))
