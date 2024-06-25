N, M, K = map(int, input().split())

dp = [[0] * 15 for _ in range(15)]

for n in range(15):
    for m in range(15):
        if n == m == 0:
            dp[n][m] = 1
        else:
            dp[n][m] = dp[n - 1][m] + dp[n][m - 1]

if not K:
    print(dp[N - 1][M - 1])
else:
    K -= 1
    ty, tx = K // M, K % M
    print(dp[ty][tx] * dp[N - ty - 1][M - tx - 1])