N, M = map(int, input().split())
lst = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(N):
    lst[n + 1] = [0] + list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = dp[n - 1][m] + dp[n][m - 1] - dp[n - 1][m - 1] + lst[n][m]

K = int(input())
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])