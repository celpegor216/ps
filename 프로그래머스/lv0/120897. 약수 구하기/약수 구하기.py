def solution(n):
    answer = []
    
    half = n ** 0.5
    
    for i in range(1, int(half) + 1):
        if not n % i:
            answer.append(i)
            
            if i != n // i:        
                answer.append(n // i)
            
    answer.sort()
    
    return answer