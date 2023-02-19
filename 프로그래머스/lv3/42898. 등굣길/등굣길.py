def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if not (i == 0 and j == 0):
                if [j + 1, i + 1] not in puddles:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    
    return dp[-1][-1] % 1000000007