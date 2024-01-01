T = int(input())

dp = [0] * 100001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2

for n in range(4, 100001):
    dp[n] = (dp[n - 2] + dp[n - 4] + dp[n - 6]) % 1000000009

for t in range(T):
    print(dp[int(input())])