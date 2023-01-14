def solution(x):
    answer = True
    
    total = 0
    temp = x
    
    while temp:
        total += temp % 10
        temp //= 10
    
    if x % total:
        answer = False
    
    return answer