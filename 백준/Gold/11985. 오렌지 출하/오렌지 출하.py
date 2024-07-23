# 70점...
# 해답: https://limdongjin.github.io/problemsolving/boj_11985.html#%E1%84%89%E1%85%A9%E1%84%89%E1%85%B3%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = K

for n in range(2, N + 1):
    dp[n] = dp[n - 1] + K
    minv = maxv = lst[n]

    for m in range(2, min(M, n) + 1):
        i = n - m + 1

        minv = min(minv, lst[i])
        maxv = max(maxv, lst[i])

        dp[n] = min(dp[n], dp[i - 1] + K + m * (maxv - minv))

print(dp[-1])
