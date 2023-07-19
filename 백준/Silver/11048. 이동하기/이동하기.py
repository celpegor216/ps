N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        left = dp[n][m - 1] if m > 0 else 0
        up = dp[n - 1][m] if n > 0 else 0
        leftup = dp[n - 1][m - 1] if m > 0  and n > 0 else 0

        dp[n][m] = lst[n][m] + max(left, up, leftup)

print(dp[-1][-1])