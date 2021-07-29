def leader(A):
    n = len(A)

    if n == 0:
        return False

    x = A[0]
    cnt = 1

    for i in range(1, n):
        if A[i] == x:
            cnt += 1

        elif A[i] != x and cnt > 0:
            cnt -= 1

        if cnt == 0:
            x = A[i]
            cnt = 1

    cnt = 0
    for i in range(n):
        if A[i] == x:
            cnt += 1

    if cnt > n / 2:
        return True, x
    else:
        return False


A = [1, 1, 2, 3, 4, 4, 3, 3, 3, 3, 3, 2, 3]
B = [1, 1, 2, 3, 4, 4, 3, 3, 3, 3, 2, 2, 3]
print(leader(A))
print(leader(B))
