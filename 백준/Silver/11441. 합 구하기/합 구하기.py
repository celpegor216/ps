import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for n in range(1, N + 1):
    dp[n] = dp[n - 1] + lst[n]

M = int(input())
for m in range(M):
    i, j = map(int, input().split())

    print(dp[j] - dp[i - 1])