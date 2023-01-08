# 해답: https://claude-u.tistory.com/208

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    now_w, now_v = lst[i - 1]
    for j in range(1, K + 1):
        if j < now_w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(now_v + dp[i - 1][j - now_w], dp[i - 1][j])

print(dp[-1][-1])