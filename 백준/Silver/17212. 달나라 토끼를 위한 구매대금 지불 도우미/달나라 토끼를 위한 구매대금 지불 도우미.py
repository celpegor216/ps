N = int(input())

if N == 0:
    print(0)
else:
    lst = [1, 2, 5, 7]
    dp = [[x for x in range(N + 1)], [0, 1], [0, 1], [0, 1]]

    for i in range(1, 4):
        for j in range(2, N + 1):
            if j >= lst[i]:
                dp[i].append(min(dp[i - 1][j], dp[i][j - lst[i]] + 1))
            else:
                dp[i].append(dp[i - 1][j])

    print(dp[-1][-1])