N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[1][lst[0][0]] = lst[0][1]
dp[1][lst[0][2]] = lst[0][3]

for n in range(N):
    for k in range(1, K + 1):
        if dp[n][k] > 0:

            if k + lst[n][0] <= K:
                dp[n + 1][k + lst[n][0]] = max(dp[n + 1][k + lst[n][0]], dp[n][k] + lst[n][1])
            if k + lst[n][2] <= K:
                dp[n + 1][k + lst[n][2]] = max(dp[n + 1][k + lst[n][2]], dp[n][k] + lst[n][3])

print(max(dp[-1]))