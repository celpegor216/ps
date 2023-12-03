N = int(input())
lst = list(map(int, input().split()))

dp = [0] + [j * (1 + abs(lst[0] - lst[j])) for j in range(1, N)]

for i in range(1, N):
    for j in range(i + 1, N):
        dp[j] = min(dp[j], max(dp[i], (j - i) * (1 + abs(lst[i] - lst[j]))))

print(dp[-1])