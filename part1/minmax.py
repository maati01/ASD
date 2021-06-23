#wyszukiwanie min, max przy uzyciu maksymalnie 1,5n porównań

def min_max(arr):
    dl = len(arr)
    if dl % 2 != 0: #rozwiazanie problemu z nieparzysta iloscia elementów
        dl = dl-1
    if arr[0] >= arr[1]:
        min_arr = arr[1]
        max_arr = arr[0]
    else:
        min_arr = arr[0]
        max_arr = arr[1]
    for i in range(2,dl,2):
        if arr[i] >= arr[i+1]:
            if min_arr > arr[i+1]:
                min_arr = arr[i+1]
            if max_arr < arr[i]:
                max_arr = arr[i]
        else:
            if min_arr > arr[i]:
                min_arr = arr[i]
            if max_arr < arr[i+1]:
                max_arr = arr[i+1]


    if  arr[-1] > max_arr: #sprawdzenie ostaniego elementu pominiętego w petli
        max_arr = arr[-1]
    if arr[-1] < min_arr:
        min_arr = arr[-1]

    return min_arr,max_arr

arr = [1,2,3,100,-100,2,200,10000,-20000000000,9999999999999999999999999]
print(min_max(arr))