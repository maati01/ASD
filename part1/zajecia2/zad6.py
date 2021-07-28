def quick_sort(A,ind):
    p = 0
    r = len(A)-1
    def sub_quick_sort(A,p,r,ind):
        if p < r:
            q = partation(A,p,r,ind)
            sub_quick_sort(A,p,q-1,ind)
            sub_quick_sort(A,p+1,r,ind)

    def partation(A,p,r,ind):
        x = A[r][ind]
        i = p-1
        for j in range(p,r):
            if A[j][ind] <= x:
                i += 1
                A[i],A[j] = A[j],A[i]

        A[i+1],A[r] = A[r],A[i+1]
        return i+1

    sub_quick_sort(A,p,r,ind)
    return A

def compartments(A):
    n = len(A)
    A = quick_sort(A,1)
    A = quick_sort(A,0)

    start = (A[0][0],A[0][1])
    result = 0
    cnt = 0
    coords = None
    for i in range(1,n):
        if A[i][1] <= start[1]:
            cnt += 1
        else:
            start = A[i][0],A[i][1]
            cnt = 0

        if cnt > result:
            result = cnt
            coords = start

    if coords is None:
        return False

    return coords


A = [(1,5),(4,9),(3,6),(2,7),(4,8)]
A = [(1,7),(2,5),(3,4),(8,20),(9,19),(10,17),(9,19)]
print(compartments(A))