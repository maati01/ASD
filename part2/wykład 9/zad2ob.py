from queue import Queue

def BFS(G,Q,d,visited,parents,tab): ##zmodyfikowany bfs
    for i in Q.queue: #iteruje po stosie
        for j in range(len(G)):
            if (not visited[j] or d[j] == 1) and G[i][j] == 1:
                visited[j] = True
                d[j] = 2
                parents[j] = i
            elif d[j] == 2 and G[i][j] == 1: #gdy znajde dwojke to mam cykl
                tab.append(parents[j])
                tab.append(j)
                tab.append(i)
                return True

def BFSv2(G,s): #zmodyfikowany bfs
    n = len(G)
    Q = Queue()
    visited = [False] * n
    d = [0] * n
    d[s] = 0
    Q.put(s)
    visited[s] = True
    u = Q.get()
    parents = [None]*n

    for i in range(n):
        if not visited[i] and G[u][i] == 1:
            visited[i] = True
            d[i] = 1
            Q.put(i)
            parents[i] = u

    return Q,d,visited,parents


def cykl4(G): #indeksuje grafy od zera
    n = len(G)
    tab = []
    for i in range(n):
        tab.append(i)
        Q,d,visited,parents = BFSv2(G,i) #pierwsza fala

        if BFS(G,Q,d,visited,parents,tab): #druga fala
            tab.append(i)
            return tab
        tab = []

    return False


G = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
#G = [[0,1],[1,0]]
#G = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
#G = [[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]
print(cykl4(G))