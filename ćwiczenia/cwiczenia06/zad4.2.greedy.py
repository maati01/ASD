from queue import PriorityQueue
from math import inf
#sprawdzam jak dalego moge dojsc z itego pola, zapisując ilość skoków, i wrzucam do kolejki wartosci mniejsze od zera

def frog_greedy(A):
    n = len(A)
    queue = PriorityQueue()
    jump = 0
    energy = A[0]
    index = 0
    result = [0]

    while index + energy < n - 1:
        energy -= 1
        index += 1

        if A[index] > 0:
            queue.put((-A[index],index))

        if energy == 0 and not queue.empty():
            e, ind = queue.get()
            energy += -e
            result.append(ind)
            jump += 1

        elif energy == 0 and queue.empty():
            return inf

    jump += 1
    result.append(n-1)
    result.sort()

    return jump, result





A = [1,2,3,4,5]
B = [1,2,2,2,2,2]
C = [2,2,1,0,0]
D = [2,2,1,0,0,0]
E = [2,2,1,0,0,0,0]
F = [4,5,2,5,1,2,1,0]
G = [3,2,0,3,0,0,0,0]
print(frog_greedy(A)) #3
print(frog_greedy(B)) #3
print(frog_greedy(C)) #2
print(frog_greedy(D)) #3
print(frog_greedy(E)) #inf
print(frog_greedy(F)) #2
print(frog_greedy(G)) #3