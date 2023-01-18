def solution(n):
    answer = 0
    
    while n > 0:
        if not n % 2:
            n //= 2
        else:
            n -= 1
            answer += 1
            
    return answer