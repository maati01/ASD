from collections import deque
from math import inf
#wrzucam wierzchołki do których prowadzą darmowe krawędzie na początek kolejki
#sprawia to że mają wiekszy priorytet
#O(v^2)

def BFS(G, s, t): #indeksuje grafy od zera
    n = len(G)
    Q = deque()
    visited = [False]*n
    parents = [None]*n
    Q.append(s)
    visited[s] = True
    amount_of_fees = [inf] * n
    amount_of_fees[s] = 0

    while Q:
        u = Q.popleft()
        visited[u] = True
        for v in range(len(G[u])):
            if not visited[v] and G[u][v] != 0:
                parents[v] = u
                if G[u][v] == 'P':
                    Q.append(v)
                else:
                    Q.appendleft(v)

    return parents

def get_solution(parents,x,y):
    if parents[y] is None:
        return [x]
    else:
        return get_solution(parents,x,parents[y]) + [y]

def min_fees(G,x,y):
    parents = BFS(G,x,y)

    if parents[y] is None:
        return False
    else:
        return get_solution(parents,x,y)



#P - paid
#[0, 6, 5, 3]
G = [[0,1,0,0,'P',0,1],
     [1,0,'P',0,0,0,0],
     [0,'P',0,'P',0,0,0],
     [0,0,'P',0,'P',1,0],
     ['P',0,0,'P',0,0,0],
     [0,0,0,1,0,0,'P'],
     [1,0,0,0,0,'P',0]]
print(min_fees(G,0,3))

# [0, 2, 4, 3]
graph = [[0, 'P', 1, 0, 0],
         [0, 0, 0, 'P', 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0]]
print(min_fees(graph,0,3))

# [0, 2, 3, 1]
graph = [[0, 'P', 1, 0],
         ['P', 0, 0, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]]
print(min_fees(graph,0,1))