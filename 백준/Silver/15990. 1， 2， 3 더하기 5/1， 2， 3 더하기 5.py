T = int(input())

dp = [[0] * 100001 for _ in range(3)]

dp[0][1] = 1
dp[1][2] = 1
dp[0][3] = 1
dp[1][3] = 1
dp[2][3] = 1

for n in range(4, 100001):
    dp[0][n] = (dp[1][n - 1] + dp[2][n - 1]) % 1000000009
    dp[1][n] = (dp[0][n - 2] + dp[2][n - 2]) % 1000000009
    dp[2][n] = (dp[0][n - 3] + dp[1][n - 3]) % 1000000009

for t in range(T):
    n = int(input())
    
    print(sum([x[n] for x in dp]) % 1000000009)