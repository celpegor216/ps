N, M, W = map(int, input().split())

dp = [[0] * 31 for _ in range(31)]

for i in range(31):
    dp[i][0] = 1
    dp[0][i] = 1

for i in range(1, 31):
    for j in range(1, 31 - i):
        if i == j == 0:
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

result = 0

for i in range(W):
    for j in range(W - i):
        result += dp[N - M + i][M + j - 1]

print(result)