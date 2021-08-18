#sortowanie po wartosciach, biore najpozniejszy i najcenniejszy termin jaki moge i umieszczam go w najpóźniejszym mozliwym dla niego terminie
#terminy zaczynam od zerowego
#zakładam że najwiekszy mozliwy termin to ten z tablicy terminów
def tasks(T,D):
    n = len(T)
    deadlines = [(0,0)]*(max(D) + 1) #wolne terminy

    for i in range(n):
        T[i] = (T[i],D[i])

    T.sort(key=lambda x: x[1],reverse=True) #prawdopodobnie to nie jest konieczne
    T.sort(key=lambda x: x[0],reverse=True)

    for i in range(n):
        j = T[i][1]
        while j >= 0:
            if deadlines[j][0] == 0:
                deadlines[j] = T[i]
                break

            j -= 1

    return deadlines




T = [1,1,5,5,5,10]
D = [0,0,1,1,1,2]
print(tasks(T,D)) #[(5, 1), (5, 1), (10, 2)]
T = [1,1,5,5,5,10]
D = [1,1,2,2,2,3]
print(tasks(T,D)) #[(5, 2), (5, 2), (5, 2), (10, 3)]
T = [1,1,5,5,5,5,10]
D = [0,0,1,1,2,1,3]
print(tasks(T,D)) #[(5, 1), (5, 1), (5, 2), (10, 3)]
T = [3,10,5,4,2]
D = [2,1,2,3,0]
print(tasks(T,D)) #[(3, 2), (10, 1), (5, 2), (4, 3)]