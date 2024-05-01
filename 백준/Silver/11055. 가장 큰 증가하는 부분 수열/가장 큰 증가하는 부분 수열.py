N = int(input())
lst = list(map(int, input().split()))

dp = lst[:]

for n in range(1, N):
    for i in range(n):
        if lst[i] < lst[n]:
            dp[n] = max(dp[n], dp[i] + lst[n])

print(max(dp))