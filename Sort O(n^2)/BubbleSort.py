def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        ifSwapped = False
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                swap(arr, j, j + 1)
                ifSwapped = True

        if (ifSwapped == False):
            break
    return arr
