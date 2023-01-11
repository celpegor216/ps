def solution(balls, share):
    answer = 1
    
    for i in range(share):
        answer *= balls
        balls -= 1
    
    for i in range(share, 0, -1):
        answer //= i
    
    return answer