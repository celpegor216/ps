N = int(input())

dp = [0] * (N + 1)
dp[1] = 1

for n in range(2, N + 1):
    dp[n] = dp[n - 2] + dp[n - 1]

print(dp[-1])