def solution(targets):
    answer = 1
    
    targets.sort()
    while targets:
        now = targets.pop()
        
        while targets:
            if targets[-1][0] < now[0] + 0.1 < targets[-1][1]:
                targets.pop()
            else:
                answer += 1
                break
    
    return answer