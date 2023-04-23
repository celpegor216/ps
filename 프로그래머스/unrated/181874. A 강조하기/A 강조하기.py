def solution(myString):
    answer = ''
    
    for s in myString:
        if s in ('a', 'A'):
            answer += 'A'
        else:
            answer += s.lower()
    
    return answer