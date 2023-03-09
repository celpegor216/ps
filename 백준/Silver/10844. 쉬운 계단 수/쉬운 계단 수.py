N = int(input())

dp = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for n in range(1, N):
    for i in range(10):
        if i == 0:
            dp[n][i] = (dp[n - 1][i + 1]) % 1000000000
        elif i == 9:
            dp[n][i] = (dp[n - 1][i - 1]) % 1000000000
        else:
            dp[n][i] = (dp[n - 1][i - 1] + dp[n - 1][i + 1]) % 1000000000

print(sum(dp[-1]) % 1000000000)