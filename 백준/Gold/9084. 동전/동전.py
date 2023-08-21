T = int(input())

for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (M + 1) for _ in range(N)]

    for n in range(N):
        for m in range(M + 1):
            if m < lst[n]:
                dp[n][m] = dp[n - 1][m]
            elif m == lst[n]:
                dp[n][m] = dp[n - 1][m] + 1
            else:
                dp[n][m] = dp[n - 1][m] + dp[n][m - lst[n]]
    
    print(dp[-1][-1])