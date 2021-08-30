from zad2testy import runtests
from queue import PriorityQueue
from math import inf

#O(E*len(word))
#iteruje po slowie
#dla itej litery sprawdzam która krawedź pasuje do niej i poprzedniej
#aktualizuje najlepsze wartości dla i tej w wierzchołkach
#po każdej iteracji zeruje dystanse w wierzchołkach poza tymi zawierającymi obecną literę
#nie potrzebuje ich bo już przeszedłem do itej litery i zapisałem najlepsze opcje w wierzchołkach


def let( ch ): return ord(ch) - ord("a")

def letters( G, W ):
    L, E = G
    n = len(W)
    k = len(E)
    d = len(L)

    distance = [inf]*d

    for i in range(d): #ustawiam pierwsza litere na 0, start
        if W[0] == L[i]:
            distance[i] = 0

    for i in range(1,n):
        ind_curr, ind_prev = 0, 0
        for j in range(k):
            flag = False
            if W[i] == L[E[j][0]] and W[i - 1] == L[E[j][1]]:
                ind_prev = E[j][1]
                ind_curr = E[j][0]
                flag = True
            if W[i-1] == L[E[j][0]] and W[i] == L[E[j][1]]:
                ind_prev = E[j][0]
                ind_curr = E[j][1]
                flag = True
            if flag:
                if distance[ind_curr] > distance[ind_prev] + E[j][2]:
                    distance[ind_curr] = distance[ind_prev] + E[j][2]

        for l in range(d):
            if L[ind_curr] != L[l]:
                distance[l] = inf

    return min(distance)

runtests( letters )