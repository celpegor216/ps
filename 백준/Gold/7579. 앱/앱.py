N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
app = [[cost[n], memory[n]] for n in range(N)]
app.sort()

total_cost = sum(cost)

dp = [[0] * (total_cost + 1) for _ in range(N)]

for n in range(N):
    for k in range(total_cost + 1):
        if k < app[n][0]:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - app[n][0]] + app[n][1])

for k in range(total_cost + 1):
    if dp[-1][k] >= M:
        print(k)
        break