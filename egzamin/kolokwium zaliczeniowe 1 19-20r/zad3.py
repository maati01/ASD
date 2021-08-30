from zad3testy import runtests
from math import inf

#ide lewym i prawym indeksem tak żeby mieć k - 1 róznych wartości
#gdy nie mam k - 1 ide prawym i rozserzam
#jak mam za duzo ide lewym i zmniejszam
#dzieki mapowaniu i uzyciu binary searcha O(nlogk)

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

def longest_incomplete( A, k ):
    n = len(A)

    uniq = [inf]*k
    counter = [0]*k
    uniq[0] = min(A)

    for i in range(n): #mapuje
        if binary_search(uniq,A[i]) == -1: #sprawdzam czy wartość występuje
            last = 0
            curr = 0
            for j in range(1,k): #jesli nie wstawiam w odpowiednie miejsce
                if uniq[j] <= A[i]:
                    continue
                else:
                    curr = uniq[j]
                    uniq[j] = A[i]
                    last = j
                    break
            for j in range(last + 1,k-1): #wiekrze wartości przepycham
                next = uniq[j+1]
                uniq[j] = curr
                curr = next

    first_ind = 0
    second_ind = 0
    cnt = 1 #ilość różncyh wartości
    result = 0
    counter[binary_search(uniq,A[0])] = 1

    while second_ind < n - 1:
        second_ind += 1
        ind = binary_search(uniq,A[second_ind])

        if counter[ind] == 0:
            cnt += 1
        counter[ind] += 1

        if cnt <= k - 1:
            continue

        while first_ind + 1 <= second_ind:
            ind = binary_search(uniq, A[first_ind])

            if second_ind - first_ind > result:
                result = second_ind - first_ind

            if counter[ind] > 0:
                counter[ind] -= 1

            if counter[ind] == 0:
                cnt -= 1

            first_ind += 1
            ind = binary_search(uniq,A[first_ind])

            if counter[ind] == 0:
                cnt += 1

            if cnt == k - 1:
                break

    return result

runtests( longest_incomplete )