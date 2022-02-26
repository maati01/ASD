from queue import Queue


def BFS(G, s): #indeksuje grafy od zera
    n = len(G)
    Q = Queue()
    visited = [False]*n
    d = [-1]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(len(G[u])):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                d[v] = d[u] + 1
                parents[v] = u
                Q.put(v)

    return parents

def get_result(parents,x):
    if parents[x] is None: return [0]
    else: return get_result(parents,parents[x]) + [x]

def shortest_path(G,x,y):
    parents = BFS(G, x)

    if parents[y] is None:
        return False

    else:
        return get_result(parents, y)

#[0, 1, 3, 4, 5]
graph = [[0,1,1,0,0,0],
         [1,0,1,1,0,0],
         [1,1,0,1,0,0],
         [0,1,1,0,1,0],
         [0,0,0,1,0,1],
         [0,0,0,0,0,1]]
print(shortest_path(graph,0,5))

#[0, 1, 3, 5]
graph = [[0,1,1,0,0,0],
         [1,0,1,1,0,0],
         [1,1,0,1,0,0],
         [0,1,1,0,1,1],
         [0,0,0,1,0,1],
         [0,0,0,0,0,1]]
print(shortest_path(graph,0,5))

#False
graph = [[0,1,1,0,0,0],
         [1,0,1,1,0,0],
         [1,1,0,1,0,0],
         [0,1,1,0,0,0],
         [0,0,0,1,0,1],
         [0,0,0,0,0,1]]
print(shortest_path(graph,0,4))