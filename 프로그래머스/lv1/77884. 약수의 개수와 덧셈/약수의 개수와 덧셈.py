def solution(left, right):
    answer = 0
    
    memo = [0] * (right + 1)
    
    for i in range(1, right + 1):
        j = 1
        while i * j <= right:
            memo[i * j] += 1
            j += 1
    
    for i in range(left, right + 1):
        if not memo[i] % 2:
            answer += i
        else:
            answer -= i
    
    return answer