def partation(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def select(A,a,b,i):
    if a == b:
        return A[a]

    q = partation(A,a,b)

    #k = q - a + 1 jesli chce k tą liczbe co do wartosci

    if i == q: #wynikiem jest element rodzielający
        return A[q]

    elif i < q:
        return select(A,a,b - 1,i)

    else:
        return select(A,a+1,b,i) #(k-i)

def section(T,p,q):
    B = []
    p = select(T,0,len(T)-1,p)
    q = select(T,0,len(T)-1,q)
    for i in range(len(T)):
        if T[i] >= p and T[i] <=q:
            B.append(T[i])

    return B

#print(section([3,2,1,5,6,4,7,0,9,8,10],1,1))