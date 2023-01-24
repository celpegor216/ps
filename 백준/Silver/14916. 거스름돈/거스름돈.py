# n | 1  | 2  | 3  | 4  | 5  | 6 | 7 | ...
# 2 | -1 | 1  | -1 | 2  | -1 |
# 5 | -1 | -1 | -1 | -1 | 1  |
# t | -1 | 1  | -1 | 2  | 1  |


n = int(input())
n += 1

INF = 10e8
dp = [[INF] * n for _ in range(3)]
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0

for i in range(2, n):
    dp[0][i] = dp[2][i - 2] + 1
    if i >= 5:
        dp[1][i] = dp[2][i - 5] + 1

    dp[2][i] = min(dp[0][i], dp[1][i])

print(dp[2][-1] if dp[2][-1] < INF else -1)