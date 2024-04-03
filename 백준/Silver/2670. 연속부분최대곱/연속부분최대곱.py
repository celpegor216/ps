N = int(input())
lst = [float(input()) for _ in range(N)]

dp = [0] * N
dp[0] = lst[0]

for n in range(1, N):
    dp[n] = max(dp[n - 1] * lst[n], lst[n])

print(f'{max(dp):0.3f}')