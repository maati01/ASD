from zad3testy import runtests
from queue import Queue

#zadanie podobne do żaby zbigniewa
#rekurencyjnie obliczam powierzchnie plamy i zapisuje w tablicy T w wierszu 0
#ide i wrzucam do kolejki plamy, tracąc 1 litr paliwa za każdym przejściem na pole w prawo
#jeśli nie dotarłem do końca a brakuje mi paliwa to biore plamę z kolejki i dodaje jej indeks do rezultatu
#ostatni test ma 2 rozwiązania
#O(n*m)

def merge_the_stain(T,i,j,last):#funkcja oblicza powierzchnie plamy
    val = 0
    if i >= len(T) or i < 0 or j >= len(T[0]) or j < 0 or T[i][j] == 0:
        return 0

    if last != 'down':
        val += merge_the_stain(T,i+1,j,'up')
    if last != 'up':
        val += merge_the_stain(T,i-1,j,'down')
    if last != 'right':
        val += merge_the_stain(T,i,j - 1,'left')
    if last != 'left':
        val += merge_the_stain(T,i,j+1,'right')

    val += T[i][j]
    T[i][j] = 0

    return val

def plan(T):
    n = len(T[0])
    result = [0]

    for i in range(n):
        if T[0][i] != 0 or T[0][i - 1] != 0:
            T[0][i] = merge_the_stain(T,0,i,'start')

    Q = Queue()
    fuel = T[0][0]
    i = 1

    while fuel + i < n:
        if T[0][i] != 0:
            Q.put((T[0][i],i))

        if fuel == 0:
            fuel, ind = Q.get()
            result.append(ind)

        i += 1
        fuel -= 1

    return result

runtests(plan)
