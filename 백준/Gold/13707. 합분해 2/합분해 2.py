N, K = map(int, input().split())

dp = [[1] * (N + 1), []]
tmp = [0] * (N + 1)
tmp[0] = 1
dp[1] = tmp[:]

for k in range(K - 1):
    for n in range(1, N + 1):
        dp[1][n] = (dp[1][n - 1] + dp[0][n]) % (10 ** 9)
    
    dp[0] = dp[1][:]
    dp[1] = tmp[:]

print(dp[0][-1])