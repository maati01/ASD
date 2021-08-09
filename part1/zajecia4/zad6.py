from math import inf

#O(n)

def find_bucket(A, n, minimum, maximum, i):  # funkcja przydziela bucketa uwzględniająć liczby ujemne
    _i = int((A[i] - minimum) / (maximum - minimum) * n)
    if _i == n: _i -= 1

    return _i


def the_biggest_difference(A):
    n = len(A)
    max_ = max(A)
    min_ = min(A)
    buckets = [[] for _ in range(n)]

    for i in range(n):#O(n)
        buckets[find_bucket(A, n, min_, max_, i)].append(A[i])

    result = -inf
    x = None
    y = None
    last_max = -inf
    last_min = inf

    for j in range(len(buckets[0])):
        if buckets[0][j] > last_max:
            last_max = buckets[0][j]

    for j in range(len(buckets[n - 1])):
        if buckets[n - 1][j] < last_min:
            last_min = buckets[n - 1][j]

    for i in range(1, n - 1):
        temp_min = inf
        temp_max = -inf
        for j in range(len(buckets[i])): #k*n -> O(n), gdzie k to stała
            if buckets[i][j] > temp_max:
                temp_max = buckets[i][j]
            if buckets[i][j] < temp_min:
                temp_min = buckets[i][j]
        if temp_min - last_max > result and len(buckets[i]) != 0:
            result = temp_min - last_max
            x = temp_min
            y = last_max

        if len(buckets[i]) != 0:
            last_max = temp_max

    if last_min - last_max > result:
        result = last_min - last_max
        x = last_min
        y = last_max

    return result, x, y


A = [3, 2, 5, -6, 1, 5, 0, -10, 6, 12, 13]
B = [3, 2, 5, -5, 1, 5, 0, -10, 6, 12, 13]
C = [2, 5, -5, 1, 5, 0, 6, 12, 13, -12,-13,-14]
print(the_biggest_difference(A))
print(the_biggest_difference(B))
print(the_biggest_difference(C))
