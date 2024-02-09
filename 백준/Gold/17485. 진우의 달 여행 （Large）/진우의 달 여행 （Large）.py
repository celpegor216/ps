N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[[21e8] * 3 for _ in range(M)] for _ in range(N)]
before = [[0, 1], [-1, 1], [-1, 0]]

for m in range(M):
    for i in range(3):
        dp[0][m][i] = lst[0][m]

for n in range(1, N):
    for m in range(M):
        for i in range(3):
            for b in before[i]:
                if 0 <= m + b < M:
                    dp[n][m][i] = min(dp[n][m][i], dp[n - 1][m + b][b + 1] + lst[n][m])

result = 21e8

for m in range(M):
    for i in range(3):
        result = min(result, dp[-1][m][i])

print(result)