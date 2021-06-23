from math import inf

def decreasing_edges_path(G,s,t):
    n = len(G)
    G = sorted(G,key = lambda x: x[2], reverse=True)
    res = []

    d = [inf]*n
    d[s] = 0
    prev = [inf]*n #ostatnia waga
    parents = [None]*n

    for u,v,w in G:
        if d[v] > d[u] + w and prev[u] != w:
            d[v] = d[u] + w
            parents[v] = u
            prev[v] = w

    if d[t] != None:
        temp = d[t]
        res.append(t)
        while(parents[t] != None):
            res.append(parents[t])
            t = parents[t]
        return res,temp
    else:
        return None

 #([0, 2, 4, 3], 12)
graph = [[0, 1, 10],
         [0, 2, 5],
         [1, 0, 10],
         [1, 2, 1],
         [1, 3, 3],
         [1, 4, 2],
         [2, 0, 5],
         [2, 1, 1],
         [2, 3, 6],
         [2, 4, 4],
         [3, 1, 3],
         [3, 2, 6],
         [3, 4, 3],
         [3, 5, 2],
         [4, 1, 2],
         [4, 2, 4],
         [4, 3, 3],
         [4, 5, 1],
         [5, 3, 2],
         [5, 4, 1]]

#print(decreasing_edges_path(graph, 0, 3))

# ([0, 3, 2], 7)
'''graph = [[0, 1, 10],
         [1, 2, 10],
         [0, 3, 4],
         [3, 2, 3]]'''

#print(decreasing_edges_path(graph, 0, 2))

# ([0, 1, 6, 5, 4, 3, 2], 39)
'''graph = [[0, 1, 9],
         [1, 0, 9],
         [1, 2, 10],
         [1, 6, 8],
         [2, 1, 10],
         [2, 3, 4],
         [3, 2, 4],
         [3, 4, 5],
         [4, 3, 5],
         [4, 5, 6],
         [5, 4, 6],
         [5, 6, 7],
         [6, 2, 8],
         [6, 5, 7]]'''

print(decreasing_edges_path(graph, 0, 2))