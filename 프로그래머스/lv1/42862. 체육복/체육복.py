def solution(n, lost, reserve):
    answer = 0
    
    lst = [1] * (n + 1)
    
    for item in lost:
        lst[item] -= 1
    
    for item in reserve:
        lst[item] += 1
    
    for i in range(1, n + 1):
        if lst[i] == 0:
            if lst[i - 1] == 2:
                lst[i] = 1
                lst[i - 1] = 1
            elif i < n and lst[i + 1] == 2:
                lst[i] = 1
                lst[i + 1] = 1
        
    for i in range(1, n + 1):
        if lst[i] > 0:
            answer += 1
    
    return answer