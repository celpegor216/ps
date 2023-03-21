# 해답: https://m.blog.naver.com/chanmuzi/222845284125

def solution(n):
    answer = 0
    
    if not n % 2:
        n //= 2
        
        dp = [0] * (n + 1)
        dp[1] = 3
                
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] * 3 + sum(dp[:i - 1]) * 2 + 2) % 1000000007
        
        answer = dp[n]
    
    return answer