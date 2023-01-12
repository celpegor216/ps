def solution(a, b):
    answer = 1
    
    max_ys = 1
    
    for i in range(1, max(a, b)):
        if not a % i and not b % i:
            max_ys = i
            
    b //= max_ys
    
    while b:
        if not b % 2:
            b //= 2
        elif not b % 5:
            b //= 5
        else:
            break
    
    if b != 1:
        answer = 2
    
    return answer