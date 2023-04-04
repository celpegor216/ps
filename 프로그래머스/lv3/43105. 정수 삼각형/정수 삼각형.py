def solution(triangle):
    answer = 0
    length = len(triangle)
    
    dp = [[0] * length for _ in range(length)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, length):
        for j in range(i + 1):
            if j == 0:            
                max_v = dp[i - 1][j]
            elif j == i:
                max_v = dp[i - 1][j - 1]
            else:
                max_v = max(dp[i - 1][j], dp[i - 1][j - 1])
                
            dp[i][j] = triangle[i][j] + max_v
    
    return max(dp[-1])