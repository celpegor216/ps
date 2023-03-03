def solution(n, m, section):
    answer = 0
    length = len(section)
    
    if m == 1:
        return length
    
    section = section[::-1]
    now = section.pop()
    
    while now + m < n:
        answer += 1
        while section:
            if section[-1] < now + m:
                section.pop()
            else:
                break
        if section:
            now = section[-1]
        else:
            break
    
    if section:
        answer += 1
    
    return answer