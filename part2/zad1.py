from zad1testy import runtests

#Mateusz Powęska
#f(i,j) = max studentów w przedziale od i do j akademikó
#f(i,j) = jesli nie nachodzą sie akademiki to F[i][j] = F[i][j - 1] + studenci w j
#         jesli sie nachodzą to F[i][j] = max(F[i][j],F[i][j - k] + studenci w j) gdzie k (1, j)
#funckja sprawdza maksymalnych studentów przedziale i gdy nachodzą na siebie to sprawdza ostatni mozliwy wynik gdzie się nie nachodzą
#zlożonośc zlożoność pesymistyczna to n^3 ze wzgledu na iteracje po i oraz j oraz k gdy przedzialy sie nachodzą

def students(T,i):
    return (T[i][2] - T[i][1])*T[i][0]

def select_buildings(T, p):
    n = len(T)
    T.sort(key = lambda x: x[2]) #sortuje po b
    T.sort(key = lambda x: x[1]) #sortuje po a

    F = [[0]*n for _ in range(n)]
    D = [[0]*n for _ in range(n)] #ostatni akademik w uzyty
    cost = [[0]*n for _ in range(n)] #koszt na polach
    result = [[-1]*n for _ in range(n)] #indeks z którego zaczynam rozwiazanie
    result1 = []



    for i in range(n):
        F[i][i] = students(T, i)
        cost[i][i] += T[i][3]

    D[0][0] = 0 #trzymam ostatni akademik jaki wziąłem

    for i in range(n):
        for j in range(max(1,i),n):
            if T[D[i][j - 1]][2] < T[j][1]: #jesli poprzedni z nastepnym sie nie nachodzą
                F[i][j] = F[i][j - 1] + students(T,j)
                D[i][j] = j
                if j != i:
                    cost[i][j] += cost[i][j-1] + T[j][3]
                    result[i][j] = j - 1
            else:
                for k in range(1,j + 1):
                    if T[D[i][j - k]][2] < T[j][1]: #sprawdzam ostatni przedział gdzie się nie nachodzą
                        F[i][j] = max(F[i][j],F[i][j - k] + students(T,j))
                        cost[i][j] += cost[i][j-k] + T[k][3]
                        result[i][j] = j - k




    end = (0,0,0) #krotka trzymajaca wynik
    for i in range(n):
        for j in range(n):
            if F[i][j] > end[0] and cost[i][j] < p:
                end = (F[i][j],i,j)


    j = end[2]
    i = end[1]


    while result[i][j] != -1: #odczytuje wynik
        result1.append(j)
        j = j-1

    result1.append(j)


    return result1


runtests( select_buildings )
