def solution(n):
    answer = ''
    
    i = 1
    while n:
        answer += str(n % (3 ** i))
        n //= 3 ** i
        
    answer = int(answer, 3)
    
    return answer