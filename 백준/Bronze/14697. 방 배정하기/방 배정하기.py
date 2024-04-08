tmp = list(map(int, input().split()))
rooms = sorted(tmp[:3])
N = tmp[-1]

dp = [[0] * (N + 1) for _ in range(3)]

for i in range(3):
    for j in range(N + 1):
        if j < rooms[i]:
            dp[i][j] = dp[i - 1][j]
        elif j == rooms[i]:
            dp[i][j] = 1
        else:
            dp[i][j] = 1 if dp[i][j - rooms[i]] or dp[i - 1][j] else 0

print(dp[-1][-1])