from zad2testy import runtests
from math import inf

def let( ch ): return ord(ch) - ord("a")

def letters( G, W ): #G(L,E)
    L,E = G
    n = len(L)
    w = len(W)
    e = len(E)
    dist = [inf]*n
    new_G = [[] for _ in range(n)]

    for i in range(n):
        if W[0] == L[i]:
            dist[i] = 0

    for i in range(e):
        u,v,val = E[i]
        new_G[E[i][0]].append((u,v,val))
        new_G[E[i][1]].append((v,u,val))

    for i in range(w-1):
        for j in range(n):
            for e in new_G[j]:
                v, u, val = e
                if W[i] == L[v] and W[i+1] == L[u]:
                    if dist[u] > val + dist[v]:
                        dist[u] = val + dist[v]
        for k in range(n):
            dist[k] = inf if L[k] != W[i+1] else dist[k]

    res = inf
    for i in range(n):
        if L[i] == W[w-1] and dist[i] < res:
            res = dist[i]

    return res
runtests( letters )
