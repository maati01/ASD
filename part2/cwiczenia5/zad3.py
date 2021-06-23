def longest(A, B):
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    l = 0

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] == 1:
                l += 1
                print(A[i], end='')
                break
    print("\n", l)


A = 'DAMIAN'
B = 'XDITN'
longest(A, B)
