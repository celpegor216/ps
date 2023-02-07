N = int(input())

INF = 21e8
dp = [[(INF, 0)] * (N + 1) for _ in range(4)]

if N == 1:
    print(0)
    print(1)
elif N == 2:
    print(1)
    print(2, 1)
elif N == 3:
    print(1)
    print(3, 1)
elif N > 3:
    dp[3][1] = (0, 0)
    dp[1][2] = (1, 1)
    dp[3][2] = (1, 1)
    dp[0][3] = (1, 1)
    dp[3][3] = (1, 1)
    for i in range(4, N + 1):
        if not i % 3:
            dp[0][i] = (dp[3][i // 3][0] + 1, i // 3)
        if not i % 2:
            dp[1][i] = (dp[3][i // 2][0] + 1, i // 2)
        dp[2][i] = (dp[3][i - 1][0] + 1, i - 1)
        
        minv = INF
        minidx = 0
        for j in range(3):
            if minv > dp[j][i][0]:
                minv = dp[j][i][0]
                minidx = dp[j][i][1]
        
        dp[3][i] = (minv, minidx)
    
    path = [N]
    idx = N
    
    while idx > 1:
        path.append(dp[3][idx][-1])
        idx = dp[3][idx][-1]
    
    print(dp[-1][-1][0])
    print(*path)