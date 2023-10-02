N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[[21e8] * 3 for _ in range(3)] for _ in range(N)]

dp[0][0][0] = lst[0][0]
dp[0][1][1] = lst[0][1]
dp[0][2][2] = lst[0][2]

for n in range(1, N):
    for i in range(3):
        dp[n][0][i] = min(dp[n - 1][1][i], dp[n - 1][2][i]) + lst[n][0]
    for i in range(3):
        dp[n][1][i] = min(dp[n - 1][0][i], dp[n - 1][2][i]) + lst[n][1]
    for i in range(3):
        dp[n][2][i] = min(dp[n - 1][0][i], dp[n - 1][1][i]) + lst[n][2]

result = 21e8
for i in range(3):
    for j in range(3):
        if i != j:
            result = min(result, dp[-1][i][j])

print(result)