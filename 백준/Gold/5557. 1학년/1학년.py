N = int(input())
lst = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][lst[0]] = 1

for n in range(1, N - 1):
    for i in range(21):
        if dp[n - 1][i] != 0 and 0 <= i + lst[n] < 21:
            dp[n][i + lst[n]] += dp[n - 1][i]
        if dp[n - 1][i] != 0 and 0 <= i - lst[n] < 21:
            dp[n][i - lst[n]] += dp[n - 1][i]

print(dp[-1][lst[-1]])