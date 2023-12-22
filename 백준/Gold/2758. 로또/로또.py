# dp인 건 알았는데 점화식을 잘못 세움
# 해답: https://ddiyeon.tistory.com/65

T = int(input())

dp = [[0] * 2001 for _ in range(11)]
dp[0] = [1] * 2001

for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j // 2]

for t in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])