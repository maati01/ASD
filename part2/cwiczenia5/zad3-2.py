#zadanie 3 tylko z uzyciem binary searcha co daje nlogn

def binary_search(A, l, r, key): #funkcja szuka gdzie wstawic wartosc (z geeks)
    while (r - l > 1):

        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def better_longest(A):
    n = len(A)
    end = [0 for _ in range(n + 1)] #trzymam końce podciągów

    end[0] = A[0] #pierwszy koniec to pierwszy element
    lenght = 1

    for i in range(1, n):

        if (A[i] < end[0]):

            end[0] = A[i]

        elif (A[i] > end[lenght - 1]):

            end[lenght] = A[i]
            lenght += 1

        else:

            end[binary_search(end, -1, lenght-1, A[i])] = A[i] #szukam optymalnego miejsca miedzy poczatkiem i koncem, ktorego koniec jest maksymalny

    print(end)

    return lenght


#A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
A = [1,3,2,3,-11,4,5,6,1245]
print(better_longest(A))
