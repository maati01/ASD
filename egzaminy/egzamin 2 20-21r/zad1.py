from zad1testy import runtests

#mapuje punkty z przedziałów
#przedziały traktuje jako 'krawędzie'
#sortuje rosnąco
#iteruje po przedziałach
#sprawdzam czy moge dojść do końca itego przedziału od startu x
#sortuje malejąco
#iteruje po przedziałach
#sprawdzam czy mogę dojść do początku itego przedziału od końca y
#sprawdzam przedziały
#jesli w krawędzi [s,t] mogę dojść do punktu s oraz t z końca i początku to
#oznacza, że należy do rozwiązania
#dzięki mapowaniu i szukaniu binary searchem punktów na krańcach przedziałów
#O(nlogn)


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


def generate_pts_from_ranges(A):
    pts_tmp = []
    for e in A:
        pts_tmp.append(e[0])
        pts_tmp.append(e[1])

    pts_tmp.sort()

    pts = [pts_tmp[0]]
    for e in pts_tmp:
        if e != pts[-1]:
            pts.append(e)

    return pts


def intuse(I, x, y):
    n = len(I)
    copy_I = [[0, 0]] * n  # x,y
    points = generate_pts_from_ranges(I)
    k = len(points)
    starts = [0]*k
    ends = [0]*k

    for i in range(n):
        copy_I[i] = [I[i][0], I[i][1]]

    copy_I.sort(key=lambda x: x[0])
    for i in range(n):
        ind1 = binary_search(points,copy_I[i][0])
        ind2 = binary_search(points,copy_I[i][1])

        if copy_I[i][0] == x:
            starts[ind1] = 1

        if starts[ind1]:
            starts[ind2] = 1

    copy_I.sort(key=lambda x: x[0], reverse=True)

    for i in range(n):
        ind1 = binary_search(points, copy_I[i][0])
        ind2 = binary_search(points, copy_I[i][1])

        if copy_I[i][1] == y:
            ends[ind2] = 1

        if ends[ind2]:
            ends[ind1] = 1

    result = []
    for i in range(n):
        ind1 = binary_search(points,I[i][0])
        ind2 = binary_search(points,I[i][1])

        if starts[ind1] and starts[ind2] and ends[ind1] and ends[ind2]:
            result.append(i)

    return result

runtests(intuse)
