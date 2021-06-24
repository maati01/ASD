from zad1testy import runtests
from collections import deque

#zapisuje indeksy liter slowa x w tablicy pomocniczej
#iteruje po y, zdejmuje za pomocą popleft w czasie O(1) pierwszy indeks pod jakim pojawiła sie litera w poprzednim słowie
#sprawdzam czy roznica indeksów sie zgadza z zwarunkami zadania

def tanagram(x, y, t):
    n = len(x)
    k = len(y)
    if n != k:
        return False

    T = [deque() for _ in range(27)]
    for i in range(n):
        T[ord(x[i]) - 97].append(i)

    for i in range(k):
        temp = ord(y[i]) - 97
        ind = T[temp].popleft()
        if ind is None:
            continue
        elif abs(ind - i) > t:
            return False

    return True

runtests( tanagram )
