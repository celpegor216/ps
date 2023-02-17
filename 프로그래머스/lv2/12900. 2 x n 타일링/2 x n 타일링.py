def solution(n):
    answer = 0
    
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        before_2 = 1
        before_1 = 2
        
        for i in range(n - 2):
            answer = (before_2 + before_1) % 1000000007
            before_2 = before_1
            before_1 = answer
    
    return answer