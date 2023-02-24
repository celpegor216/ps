def solution(x, y, n):
    INF = 21e8
    
    dp = [[INF] * (y + 1) for _ in range(4)]
    dp[0][x] = 0
    dp[1][x] = 0
    dp[2][x] = 0
    dp[3][x] = 0
    
    for i in range(x, y + 1):
        dp[0][i] = dp[3][i - n] + 1
        if not i % 2:
            dp[1][i] = dp[3][i // 2] + 1
        if not i % 3:
            dp[2][i] = dp[3][i // 3] + 1
        
        dp[3][i] = min(dp[0][i], dp[1][i], dp[2][i])
    
    return dp[-1][-1] if dp[-1][-1] < INF else -1