def mentos(tab):
    n = len(tab)

    dp = [[0 for _ in range(n)] for _ in range(n)]
    pref = [i for i in tab]

    for i in range(n):
        dp[i][i] = tab[i]
        if i > 0:
            pref[i] += pref[i-1]

    for l in range(2, n):
        for i in range(n-l):
            dp[i][i+l] = pref[i+l] - pref[i]
            dp[i][i+l] -= min(dp[i+1][i+l], dp[i][i+l-1])

    for i in dp:
        print(i)

    print(pref)
    print(dp[0][n-1])

board = [1,4,5,6,7,3,1]

mentos(board)