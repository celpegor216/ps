def solution(n):
    answer = 0
    
    half = int(n ** 0.5)
    
    for i in range(1, half + 1):
        if not n % i:
            answer += i
            
            if i != n // i:
                answer += n // i
    
    return answer