def solution(lines):
    answer = 0
    
    bucket = [0] * 201
    
    for a, b in lines:
        for i in range(a, b):
            bucket[i + 100] += 1
    
    for i in range(201):
        if bucket[i] > 1:
            answer += 1
    
    return answer