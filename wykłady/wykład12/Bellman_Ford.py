from math import inf

#uwaga na ujemne cykle
#graf musi byc skierowany
#O(V^3) dla macierzowej
#O(V*E) dla list sasiedztwa
def bellman_ford(G,v): #reprezentacja macierzowa
    n = len(G)
    d = [inf]*n
    parents = [None]*n
    d[v] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G[j][k] != 0 and d[k] > d[j] + G[j][k]:  # relaksacja
                    d[k] = d[j] + G[j][k]
                    parents[k] = j


    for i in range(n):
        for j in range(n):
            if G[i][j] != 0 and d[j] > d[i] + G[i][j]: #weryfikacja czy jest ujemny cykl
                return None

    return d

G = [[0,1,1,-2],
     [1,0,3,2],
     [1,3,0,1],
     [-2,2,1,0]]
# None
'''G = [[0, -1, -1],
    [-1, 0, 0],
    [1, 0, 0]]'''

# [0, 5, 5, 7, 9, 8]
G = [[0, 0, 10, 0, 0, 8],
         [0, 0, 0, 2, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, -2, 0, 0, 0],
         [0, -4, 0, -1, 0, 0],
         [0, 0, 0, 0, 1, 0]]

G = [[0, 9, 0, 0, 0, 0, 0],
    [9, 0, 10, 0, 0, 0, 8],
    [0, 10, 0, 4, 0, 0, 0],
    [0, 0, 4, 0, 5, 0, 0],
    [0, 0, 0, 5, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 7],
    [0, 8, 0, 0, 0, 7, 0]]

print(bellman_ford(G,0))

def bellman_ford_lists(G,v): #reprezentacja listowa
    n = len(G)
    d = [inf]*n
    parents = [None]*n
    d[v] = 0

    for i in range(n): #V
        for u in range(n): #E
            for v in G[u]:
                if d[v[0]] > d[u] + v[1]:  # relaksacja
                    d[v[0]] = d[u] + v[1]
                    parents[v[0]] = u


    for u in range(n):#E
        for v in G[u]:
            if d[v[0]] > d[u] + v[1]: #weryfikacja czy jest ujemny cykl
                return None

    return d

# [0, 5, 5, 7, 9, 8]
G = [[[5, 8], [2, 10]],
    [[3, 2]],
    [[1, 1]],
    [[2, -2]],
    [[1, -4], [3, -1]],
    [[4, 1]]]
# None
'''G = [[[1, -1], [2, -1]],
    [[0, -1]],
    [[0, 1]]]'''

# None
'''G = [[[1, -4]],
    [[2, -5]],
    [[0, -2]],
    [[4, 2]],
    [[2, 1]]]'''
#print(bellman_ford_lists(G,0))