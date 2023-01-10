def solution(n):
    answer = 0
    
    half = n ** 0.5
    
    for i in range(1, int(half) + 1):
        if not n % i:
            answer += 1
    
    answer *= 2
    
    if half == int(half):
        answer -= 1
    
    return answer