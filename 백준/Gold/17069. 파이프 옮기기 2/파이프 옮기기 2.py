N = int(input())
# 빈 칸은 0, 벽은 1
lst = [[1] * (N + 1)] + [[1] + list(map(int, input().split())) for _ in range(N)]

# dp[i][j][k]: i, j에 가로/세로/대각선으로 도착할 수 있는 경우의 수
dp = [[[0] * 3 for _ in range(N + 1)] for _ in range(N + 1)]

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로
dp[1][2][0] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if lst[i][j]:
            continue

        # 가로로 도착할 수 있으려면 이전에 가로/대각선이었어야 함
        dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2]

        # 세로로 도착할 수 있으려면 이전에 세로/대각선이었어야 함
        dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]

        # 대각선으로 도착할 수 있으려면 이전에 가로/세로/대각선이었어야 함
        if not (lst[i][j - 1] or lst[i - 1][j]):
             dp[i][j][2] += sum(dp[i - 1][j - 1])

print(sum(dp[-1][-1]))