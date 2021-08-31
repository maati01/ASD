from zad2testy import runtests
from math import inf
from queue import PriorityQueue

#tablica 4d z pozycją, szybkoscią i kierunkiem przyjścia
#z kazdej pozycji ide w prawo, lewo i do przodu
#ispirowane wzorcowym rozwiązaniem od dziekana


def robot( L, A, B ):
    n = len(L)
    m = len(L[0])
    d = [[[[inf]*4 for _ in range(3)] for _ in range(m)] for _ in range(n)]
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    speed = [60,40,30]
    y, x = A
    Q = PriorityQueue()
    Q.put((0,x,y,0,0)) #dystans,x,y,ostatnia szybkość, ostatni kierunek

    while not Q.empty():
        dist,x,y,s,v = Q.get()

        if (y,x) == B:
            return dist

        if d[x][y][s][v] != inf:
            continue

        d[x][y][s][v] = dist

        if v == 3: #w prawo
            Q.put((dist + 45,x,y,0,0))
        else:
            Q.put((dist + 45, x, y, 0, v+1))

        if v == 0: #w lewo
            Q.put((dist + 45, x, y, 0, 3))
        else:
            Q.put((dist + 45, x, y, 0, v-1))

        new_x = x + directions[v][0]
        new_y = y + directions[v][1]

        if L[new_x][new_y] == 'X':
            continue
        Q.put((dist + speed[s],new_x,new_y,min(s+1,2),v))

runtests( robot )
