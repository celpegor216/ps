N = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))
hello = [[health[n], happy[n]] for n in range(N)]
hello.sort(key=lambda x: (x[0], -x[1]))

dp = [[0] * 100 for _ in range(N + 1)]

for n in range(N):
    for k in range(100):
        if k < hello[n][0]:
            dp[n + 1][k] = dp[n][k]
        else:
            dp[n + 1][k] = max(dp[n][k], dp[n][k - hello[n][0]] + hello[n][1])

print(max(dp[-1]))