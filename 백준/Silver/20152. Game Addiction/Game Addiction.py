H, N = map(int, input().split())

if H < N:
    H, N = N, H

H -= N
N = 0

dp = [[0] * (H + 1) for _ in range(H + 1)]

dp[0][0] = 1

for i in range(H + 1):
    for j in range(i, H + 1):
        if i == 0 and j == 0: continue
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[-1][-1])