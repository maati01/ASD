from testy import test

###zakłada się że nlogn bo n^2 w praktyce sie nie zdarza

def quick_sort(A):
    p = 0
    r = len(A)-1
    def sub_quick_sort(A,p,r):
        if p < r:
            q = partation(A,p,r)
            sub_quick_sort(A,p,q-1)
            sub_quick_sort(A,p+1,r)

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

#print(quick_sort([1,5,2,3,9,100,-100],0,6))

test.test_sort(quick_sort, 20 * 10 ** 6, 1, (-100, 100), True)