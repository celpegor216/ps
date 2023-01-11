def solution(n):
    answer = 1
    total = 1
    
    while 1:
        if total > n: 
            return answer - 1
        else:
            answer += 1
            total *= answer