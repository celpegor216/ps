N = int(input())
lst = [[0]] + sorted(list(map(int, input().split())) for _ in range(N))

dp = [0] * (N + 1)
dp[1] = lst[1][-1]

for n in range(2, N + 1):
    dp[n] = max(dp[n - 2] + lst[n][-1], dp[n - 1])

print(dp[-1])