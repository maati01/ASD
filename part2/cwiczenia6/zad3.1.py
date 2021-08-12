# f(i,l,r) = auta do itego indeksu  zajmując l na lewym oraz r na prawym0
# f(i,l,r) = f(i-1,l - A[i],r) or f(i-1,l,r - A[i])

def ferry(A, L):
    n = len(A)
    F = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(n)]

    F[0][A[0]][0] = 1
    #F[0][0][A[0]] = 1

    flag = True
    last = None

    if A[0] > L:
        return False

    for i in range(1, n):
        if flag:
            flag = False
            for l in range(L + 1):
                for r in range(L + 1):
                    if l >= A[i] and F[i - 1][l - A[i]][r]:
                        F[i][l][r] = F[i - 1][l - A[i]][r]
                        flag = True
                        last = i
                    elif r >= A[i] and F[i - 1][l][r - A[i]]:
                        F[i][l][r] = F[i - 1][l][r - A[i]]
                        flag = True
                        last = i

    left = []
    right = []

    i = 0
    l = 0
    r = 0
    while i <= last:
        if l + A[i] <= L and F[i][l + A[i]][r]:
            left.append(i)
            l += A[i]

        elif r + A[i] <= L and F[i][l][r + A[i]]:
            right.append(i)
            r += A[i]

        i += 1

    return len(left) + len(right), left, right


B = [1,3,2,4,1,3,2,4,6]
A = [1, 2, 3, 6, 5]
C = [2,1,2,3]
D = [10, 4, 7, 6, 5, 4, 2, 20]
E = [18, 6, 5, 11, 4, 16, 7, 8, 16, 5, 14, 8, 17, 9, 7, 1, 20, 7, 7, 4, 5, 9, 18, 20, 17, 18, 5, 5, 10, 14, 11, 9, 6, 13, 12, 15, 10, 9, 20, 2, 17, 1, 13, 7, 19, 20, 16, 6, 4, 14]


print(ferry(B, 6))
print(ferry(A, 6))
print(ferry(C, 6))
print(ferry(D, 20))
print(ferry(E, 200))
print(ferry(E, 50))
