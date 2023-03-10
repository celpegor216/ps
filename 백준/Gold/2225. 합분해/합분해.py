# 해답: https://velog.io/@cu1210/%EB%B0%B1%EC%A4%80-2225-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%A9%EB%B6%84%ED%95%B4

N, K = map(int, input().split())

dp = [[0] * N for _ in range(K)]

for i in range(N):
    dp[0][i] = 1

for j in range(K):
    dp[j][0] = j + 1

for i in range(1, K):
    for j in range(1, N):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[-1][-1])