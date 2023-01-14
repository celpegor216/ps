def solution(s):
    answer = ''
    
    i = 0
    
    for w in s:
        if w == ' ':
            answer += ' '
            i = 0
        else:
            if not i % 2:
                answer += w.upper()
            else:
                answer += w.lower()
            i += 1
        
    return answer