from testy import test


def quick_sort(A):
    p = 0
    r = len(A)-1
    def sub_quick_sort(A,p,r): #
        while p < r:
            q = partation(A,p,r)
            if q - p < r - q: #jesli lewa czesc jest mniejsza to robie rekusrje dla lewej story
                sub_quick_sort(A,p,q-1)
                p = q + 1
            else: #w przeciwnym wypadku rób prawą strone
                sub_quick_sort(A,q+1,r)
                r = q - 1


    def partation(A,p,r):
        x = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] <= x:
                i += 1
                A[i],A[j] = A[j],A[i]

        A[i+1],A[r] = A[r],A[i+1]
        return i+1

    sub_quick_sort(A,p,r)
    return A

#print(quick_sort([1]))

test.test_sort(quick_sort, 2 * 10 ** 6, 1, (-100, 100), False)