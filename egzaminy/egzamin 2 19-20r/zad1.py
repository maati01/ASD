from zad1testy import runtests
from queue import PriorityQueue

#rozwiazanie zachłanne
#mozna dynamicznie
#opis jest w rozwiązaniach z zestawów

def zbigniew( A ):
    n = len(A)
    Q = PriorityQueue()
    e = A[0] - 1
    i = 1
    jumps = 0
    while i + e < n - 1:
        if A[i] > 0:
            Q.put(-A[i])
        if e == 0 and not Q.empty():
            jumps += 1
            e = -Q.get()
        if e < 0:
            return False

        e -= 1
        i += 1

    return jumps + 1

runtests( zbigniew ) 
