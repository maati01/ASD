import math

#n*log(logn)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if x == arr[mid]:
            return mid

        elif x < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1

def insert(arr,counters,x):
    n = len(arr)

    y = 1
    for i in range(n):
        if arr[i] is None:
            arr[i] = x
            counters[i] = y
            return i + 1
        elif x <= arr[i]:
            while arr[i] is not None or i < n:
                temp1 = arr[i]
                temp2 = counters[i]
                arr[i] = x
                counters[i] = y
                x = temp1
                y = temp2
                i += 1
            return i + 1


def logn_different_numbers_sort(A):
    n = len(A)
    unique_values = [None]*(math.floor(math.log2(n)))
    counters_unique = [0]*(math.floor(math.log2(n)))
    end = 1
    unique_values[0] = A[0]
    counters_unique[0] = 1

    for i in range(1,n):
        if binary_search(unique_values[0:end],A[i]) != -1: #log(logn)
            counters_unique[binary_search(unique_values[0:end],A[i])] += 1
        else: #logn * logn, ten współczynnik działa bo n*log(logn) > logn * logn
            end = insert(unique_values,counters_unique,A[i])

    i = 0
    k = 0

    while i < n:
        if counters_unique[k] != 0:
            temp = i
            while i < counters_unique[k] + temp:
                A[i] = unique_values[k]
                i += 1
        k += 1

    return A

A = [1,2,2,2,3,1,1,1,3,3,2,3,1,1,2,3,2,3]
B = [1,2,2,2,3,4,1,1,1,3,3,2,3,1,1,2,3,2,3]
print(sorted(A))
print(logn_different_numbers_sort(A))
print(sorted(B))
print(logn_different_numbers_sort(B))
