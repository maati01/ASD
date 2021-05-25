from queue import PriorityQueue
from math import inf

def Dijkstry2(G,s):
    n=len(G)
    parent=[-1]*n
    value=[inf]*n
    value[s]=0
    q=PriorityQueue()
    q.put((0,s))


    while not q.empty():
        v,p=q.get()
        for i in G[p]:
            if value[i[0]]>v+i[1]:
                value[i[0]]=v+i[1]
                parent[i[0]]=p
                q.put((value[i[0]],i[0]))


    print(value)
    print(parent)



G = [
    [(1, 1), (2, 5)],
    [(0, 1), (2, 2), (3, 7), (4, 8)],
    [(0, 5), (1, 2), (4, 3)],
    [(1, 7), (4, 1)],
    [(1, 8), (2, 3), (3, 1)]
]
Dijkstry2(G,3)






# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None


def hamilton_DAG(V, E):
    def DFSVisit(summits, V, E, v):
        nonlocal time, T
        time += 1
        v.visited = True
        for e in E:
            if v.number == e[0] and not summits[e[1]].visited:
                summits[e[1]].parent = e[0]
                DFSVisit(summits, V, E, summits[e[1]])
        T = [V[v.number]] + T

    summits = []
    for v in V:
        summits.append(Summit(v))
    time = 0
    T = []
    for summit in summits:
        if not summit.visited:
            DFSVisit(summits, V, E, summit)
    for i in range(1,len(T)):
        print(T[i-1][0], summits[T[i][0]].parent)
        if T[i-1][0] != summits[T[i][0]].parent:
            return False
    return True


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
E = [(0, 1), (1, 2), (1, 4), (4, 3)]
# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), '''(4, "e")]
# E = [(0, 1), (1, 2), (2,