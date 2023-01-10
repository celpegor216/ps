def solution(s1, s2):
    answer = 0
    
    if len(s1) > len(s2):
        for item in s1:
            if item in s2:
                answer += 1
    else:
        for item in s2:
            if item in s1:
                answer += 1
    
    return answer