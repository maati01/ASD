from zad3testy import runtests
from math import inf

#sortuje po koncach
#dla kazdego przedzialu wyznaczam start
#patrze na wszystkie przedzialy od najwiekszych konców, które spełniają warunki
#aktualizuje wynik
#przechodze dla kazdego przedziału po wszystkich innych

def kintersect( A, k ):
    n = len(A)

    for j in range(n):
        A[j] = A[j][0],A[j][1],j

    A.sort(key=lambda x: x[1])
    result = -inf
    tab_result = []

    for i in range(n):
        start = A[i][0]
        end = A[i][1]
        cnt = 1
        temp_result = end - start
        temp_tab = [A[i][2]]
        for j in range(n - 1, -1, -1):
            if cnt == k:
                break

            if i != j and A[j][0] <= start < A[j][1]:
                temp_result = min(end, A[j][1]) - start
                temp_tab.append(A[j][2])
                cnt += 1


        if temp_result > result and cnt == k:
            result = temp_result
            tab_result = temp_tab

    return tab_result

A = [(10, 11), (9, 12), (8, 13), (7, 14), (6, 15)]
k = 3
print(kintersect(A,k))
runtests( kintersect )