from math import *

def d(D,i,j): #funkcja liczaca odległość między punktami
    return sqrt((D[i][1]-D[j][1])**2 + (D[i][2] - D[j][2])**2)

def bitonicTSP(C):

    #C[i][j] = d(i,j)

    C = sorted(C, key=lambda x: x[1]) #sortuje po x

    n = len(C)
    F = [[inf]*n for i in range(n)]
    F[0][1] = d(C,0,1)

    up = [[] * n for i in range(n)] #górna ścieżka
    down = [[]*n for i in range(n)] #dolna ścieżka

    def tspf(i, j, F, D):
        if F[i][j] != inf:
            return F[i][j]

        if i == j - 1:
            best = inf
            for k in range(j - 1):
                best = min(best,tspf(k, j - 1,F,D) + d(D,k,j))

            F[j-1][j] = best

        else:
            F[i][j] = tspf(i, j - 1, F, D) + d(D,j-1,j)
            up.append(C[i][0])


        return F[i][j]

    for i in range(n - 1):
        res = tspf(i, n - 1,F,C) + d(C,i,n-1)

    return res

#C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
C = [["A",0,2],["B",1,1],["C",4,1],["D",5,3],["E",6,3],["F",8,3],["G",7,4],["H",2,4],["I",0.5,2.5],["J",1.5,3.5]]
print(bitonicTSP(C))