def solution(citations):
    answer = 0
    
    bucket = [0] * 10001
    
    for cit in citations:
        for i in range(cit + 1):
            bucket[i] += 1
    
    for i in range(10001):
        if bucket[i] >= i:
            answer = i
    
    return answer