# dp인데 해결 방법을 모르겠음
# 해답: https://welog.tistory.com/49

M, N = map(int, input().split())

# 이전에 북쪽/동쪽 > 다음에 회전 불가능/가능
dp = [[[[0] * 2 for _ in range(2)] for _ in range(M)] for _ in range(N)]

for n in range(N):
    dp[n][0][0][1] = 1

for m in range(M):
    dp[0][m][1][1] = 1

for n in range(1, N):
    for m in range(1, M):
        # 이전에 북쪽 > n - 1
        # 다음에 회전 불가능 > 이전에 회전한 경우(이전의 이전이 동쪽, 회전 가능)
        # 다음에 회전 가능 > 이전에 회전하지 않은 경우(이전의 이전이 북쪽)
        dp[n][m][0][0] = dp[n - 1][m][1][1]
        dp[n][m][0][1] = dp[n - 1][m][0][0] + dp[n - 1][m][0][1]

        # 이전에 동쪽 > m - 1
        # 다음에 회전 불가능 > 이전에 회전한 경우(이전의 이전이 북쪽, 회전 가능)
        # 다음에 회전 가능 > 이전에 회전하지 않은 경우(이전의 이전이 동쪽)
        dp[n][m][1][0] = dp[n][m - 1][0][1]
        dp[n][m][1][1] = dp[n][m - 1][1][0] + dp[n][m - 1][1][1]

print((sum(dp[-1][-1][0]) + sum(dp[-1][-1][1])) % 100000)