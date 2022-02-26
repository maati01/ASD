#Dana jest tablica z n liczbami całkowitymi.
#Zawiera ona bardzo dużo powtórzeń - co więcej, zaledwie O(log(n)) liczb jest unikatowe (reszta to powtórzenia).
#Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.

#rozwiazanie Igora


def insertion_sort(arr, occur_arr, elem):
    n = len(arr)
    if n < 1 or arr[n - 1] < elem:
        arr.append(elem)
        occur_arr.append(1)
        return
    j = n - 1
    arr.append(0)
    occur_arr.append(0)
    while j >= 0 and arr[j] > elem:
        arr[j + 1] = arr[j]
        occur_arr[j + 1] = occur_arr[j]
        j -= 1
    arr[j + 1] = elem
    occur_arr[j + 1] = 1


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


def rare_sort(input_arr):
    arr = []
    occur_arr = []
    for value in input_arr:
        if len(arr) == 0 or arr[len(arr) - 1] < value:
            index = -1
        else:
            index = binary_search(arr, value)  # O(n log(log n))
        if index == - 1:  # elem not in array
            insertion_sort(arr, occur_arr, value)  # O(log n * log n)
        else:
            occur_arr[index] += 1

    index = 0
    for i in range(len(arr)):
        for j in range(occur_arr[i]):
            input_arr[index] = arr[i]
            index += 1
    return input_arr