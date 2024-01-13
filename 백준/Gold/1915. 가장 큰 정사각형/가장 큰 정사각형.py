N, M = map(int, input().split())
lst = [input() for _ in range(N)]

dp =[[0] * M for _ in range(N)]

result = 0

for n in range(N):
    for m in range(M):
        if lst[n][m] == '1':
            dp[n][m] = min(dp[n - 1][m], dp[n][m - 1], dp[n- 1][m - 1]) + 1
            result = max(result, dp[n][m])

print(result ** 2)