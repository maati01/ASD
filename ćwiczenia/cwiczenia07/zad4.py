from math import inf
#new_max - max_klocek - moja_wieża, ściągam klocek tam gdzie bedzie minimum
from math import inf

def find_two_max(A):
    n = len(A)
    max_sum1 = -inf
    max_sum2 = -inf
    j = 0

    for i in range(n):
        if max_sum1 < A[i]:
            max_sum1 = A[i]
            j = i
    temp = A[j]
    A[j] = -inf

    for i in range(n):
        if max_sum2 < A[i]:
            max_sum2 = A[i]

    A[j] = temp
    return max_sum1, max_sum2


def blocks(A,start):
    n = len(A)
    sums = [0]*n
    length = [0]*n #indeksy dla klocków
    result = []

    for i in range(n):
        A[i].sort()
        sums[i] = sum(A[i])
        length[i] = len(A[i]) - 1

    max_sum1, max_sum2 = find_two_max(sums)

    temp_min = inf
    ind = 0
    while start <= max_sum1:
        for i in range(n):
            if sums[i] != max_sum1:
                if temp_min > max_sum1 - A[i][length[i]] - start and length[i] >= 0:
                    temp_min = max_sum1 - A[i][length[i]] - start
                    ind = i
            else:
                if temp_min > max_sum2 - A[i][length[i]] - start:
                    temp_min = max_sum2 - A[i][length[i]] - start
                    ind = i

        start += A[ind][length[ind]]
        sums[ind] -= A[ind][length[ind]]
        result.append((A[ind][length[ind]],ind))
        length[ind] -= 1
        max_sum1, max_sum2 = find_two_max(sums)

    return result


A = [[5,4,2,1,8],[8,6,8,5,3],[5,3,2,1],[1,1,12,1,16]]
startA = 4
print(blocks(A,startA))
B = [[8],[4,3]]
startB = 1
print(blocks(B,startB))
C = [[8],[4,5]]
startC = 1
print(blocks(C,startC))
D = [[8],[4,5]]
startD = 4
print(blocks(D,startD))
startE = 2
E = [
     [6],
     [5, 4]]
print(blocks(E,startE))
