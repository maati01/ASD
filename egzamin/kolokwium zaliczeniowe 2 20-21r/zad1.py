
#robie dwa obiegi pętli
#sprawdzam co by było gdybybym usunął i-ty prostokąt
#jeśli po usunięciu itego rezultat jest wiekszy to nadpisuje rezultat i zapamiętuje indeks itego prostokąta
#w sytacji gdy jakis protokąt wystaje poza inne porostokąty(nie ma częsci wspólnej z nimi), powierzchnia wspólna jest równa 0
#w takiej sytacji konieczne jest usnięcie tego prostokąta
#złożoność całego algorytmu O(n^2)
#zlożoność pamięciowa O(1)

from zad1testy import runtests
from math import inf

def rect(D):
    n = len(D)
    result = -inf
    temp_ind = 0
    for i in range(n):
        x1 = -inf
        y1 = -inf
        x2 = inf
        y2 = inf
        for j in range(n):
            if (D[j][2] <= x1 and D[j][3] <= y1) or (D[j][0] >= x2 and D[j][1] >= y1): #sytacja gdy prostokąt jest poza innymi
                return j

            if i != j:
                if D[j][0] > x1:
                    x1 = D[j][0]
                if D[j][1] > y1:
                    y1 = D[j][1]
                if D[j][2] < x2:
                    x2 = D[j][2]
                if D[j][3] < y2:
                    y2 = D[j][3]
        if (x2 - x1)*(y2 - y1) > result:
            result = (x2 - x1)*(y2 - y1)
            temp_ind = i

    return temp_ind

runtests( rect )