import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N

for n in range(1, N):
    dp[n] = dp[n - 1]
    if lst[n - 1] > lst[n]:
        dp[n] += 1

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())

    print(dp[y - 1] - dp[x - 1])