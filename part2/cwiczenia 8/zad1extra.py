from queue import Queue
#moge poplynąc tylko w kierunku 4 wektorów
#sprawdzam tylko mozliwe wierzchołki których jest v^2
#O(v^2)

def get_result(parents,w):
    if w is None:
        return []
    else:
        return get_result(parents,parents[w[0]][w[1]]) + [(w[0], w[1])]

def capitan(G,t):
    n = len(G)
    m = len(G[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)] #wektory o które mogę sie przesunąć na planszy
    Q = Queue()
    Q.put((0,0))
    parents = [[None]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    while not Q.empty():
        x1,y1 = Q.get()
        for i in range(4):
            x = x1 + directions[i][0]
            y = y1 + directions[i][1]
            if 0 <= x < n and 0 <= y < m and not visited[x][y] and G[x][y] > t:
                parents[x][y] = (x1,y1)
                visited[x][y] = True
                Q.put((x,y))

    if parents[n-1][m-1] is None:
        return False
    else:
        return get_result(parents,(n-1, m-1)), True


M = [[4, 3, 2],
     [1, 2, 0],
     [3, 3, 3],
     [10, 2, 1]]
T = 3
#false
print(capitan(M,T))

M = [[1, 0, 0, 1, 1, 0, 0, 1],
     [1, 1, 1, 1, 0, 1, 0, 0],
     [1, 0, 0, 1, 0, 0, 1, 0],
     [1, 0, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 0, 1, 1, 1, 1]]
T = 1
#false
print(capitan(M,T))
M = [[2, 0, 0, 1, 1, 0, 0, 1],
     [2, 2, 2, 2, 0, 1, 0, 0],
     [1, 0, 0, 2, 0, 0, 1, 0],
     [1, 0, 0, 2, 2, 0, 0, 0],
     [1, 1, 0, 0, 2, 2, 2, 2]]
T = 1
#false
print(capitan(M,T))