N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if n == 0 and m == 0:
            dp[n][m] = lst[n][m]
        elif n == 0:
            dp[n][m] = dp[n][m - 1] + lst[n][m]
        elif m == 0:
            dp[n][m] = dp[n - 1][m] + lst[n][m]
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1]) + lst[n][m]

print(dp[-1][-1])