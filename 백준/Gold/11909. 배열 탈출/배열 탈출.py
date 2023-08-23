N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(1, N):
    dp[0][i] = dp[0][i - 1] if lst[0][i - 1] > lst[0][i] else dp[0][i - 1] - lst[0][i - 1] + lst[0][i] + 1

    dp[i][0] = dp[i - 1][0] if lst[i - 1][0] > lst[i][0] else dp[i - 1][0] - lst[i - 1][0] + lst[i][0] + 1

for i in range(1, N):
    for j in range(1, N):
        left = dp[i][j - 1] if lst[i][j - 1] > lst[i][j] else dp[i][j - 1] - lst[i][j - 1] + lst[i][j] + 1
        up = dp[i - 1][j] if lst[i - 1][j] > lst[i][j] else dp[i - 1][j] - lst[i - 1][j] + lst[i][j] + 1
        dp[i][j] = min(left, up)

print(dp[-1][-1])