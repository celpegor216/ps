N, M = map(int, input().split())
K = int(input())
blocked = []

for _ in range(K):
    a, b, c, d = list(map(int, input().split()))

    if b == d and a > c:
        a, c = c, a
    elif a == c and b > d:
        b, d = d, b
    
    blocked.append((a, b, c, d))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for n in range(N + 1):
    for m in range(M + 1):
        if n != 0 and not (n - 1, m, n, m) in blocked:
            dp[n][m] += dp[n - 1][m]
        if m != 0 and not (n, m - 1, n, m) in blocked:
            dp[n][m] += dp[n][m - 1]

print(dp[-1][-1])