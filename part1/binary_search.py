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

