def solution(n):
    answer = 0
    
    memo = [0] * 1000001
    
    for i in range(2, n):
        j = 2
        while i * j <= n:
            memo[i * j] = 1
            j += 1
    
    answer = memo[2:n + 1].count(0)
    
    return answer