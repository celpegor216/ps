def solution(d, budget):
    answer = 0
    total = 0
    
    d.sort()
    
    while answer < len(d):
        total += d[answer]
        if total > budget:
            break
        else:
            answer += 1
    
    return answer