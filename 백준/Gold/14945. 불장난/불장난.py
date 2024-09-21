# 해답: https://devlibrary00108.tistory.com/398


N = int(input())
# dp[i][j]: i번째 층에서 둘 사이의 거리가 j
dp = [[0] * (N + 1) for _ in range(N + 1)]

dp[2][1] = 2

for i in range(3, N + 1):
    for j in range(1, i):
        # 둘 다 아래로 이동하거나 둘 다 대각으로 이동하는 경우,
        # 둘 사이의 거리가 변하지 않음 -> *2
        # 둘 중 하나가 대각으로 이동하는 경우, 둘 사이의 거리가 1 증가하거나 1 감소함
        dp[i][j] = (dp[i - 1][j] * 2 + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 10007

print(sum(dp[-1]) % 10007)