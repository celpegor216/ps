N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

lst.sort(key=lambda x: (x[1], x[0]))

dp = [[0] * (N + 1) for _ in range(K)]

for k in range(K):
    value, time = lst[k]

    for n in range(N + 1):
        if n < time:
            dp[k][n] = dp[k - 1][n]
        else:
            dp[k][n] = max(dp[k - 1][n], dp[k - 1][n - time] + value)

print(dp[-1][-1])