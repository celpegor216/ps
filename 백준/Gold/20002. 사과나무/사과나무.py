# dp로 도전했으나 틀렸습니다
# 해답: https://devlibrary00108.tistory.com/167

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = lst[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

result = lst[0][0]

for k in range(N):    # 정사각형 한 변의 길이 == k + 1
    for i in range(1, N + 1 - k):
        for j in range(1, N + 1 - k):
            result = max(result, dp[i + k][j + k] - dp[i - 1][j + k] - dp[i + k][j - 1] + dp[i - 1][j - 1])

print(result)