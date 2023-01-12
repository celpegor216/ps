def solution(n):
    answer = 0
    
    for i in range(n):
        answer += 1
        
        while 1:
            if not answer % 3 or '3' in str(answer):
                answer += 1
            else:
                break
            
    return answer