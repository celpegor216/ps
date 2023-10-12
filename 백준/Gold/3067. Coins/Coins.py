T = int(input())

for t in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (M + 1) for _ in range(N)]

    for i in range(N):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j]

            if j == coins[i]:
                dp[i][j] += 1
            elif j > coins[i]:
                dp[i][j] += dp[i][j - coins[i]]

    print(dp[-1][-1])