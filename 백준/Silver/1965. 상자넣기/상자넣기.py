# 해답: https://alpyrithm.tistory.com/91
# 2중 for문 필요

N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N

for n in range(1, N):
    for i in range(n):
        if lst[n] > lst[i]:
            dp[n] = max(dp[n], dp[i] + 1)

print(max(dp))