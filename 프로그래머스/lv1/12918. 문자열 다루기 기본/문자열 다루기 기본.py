def solution(s):
    answer = False
    
    if len(s) in (4, 6):
        flag = 0
        
        for i in s:
            if not '0' <= i <= '9':
                flag = 1
                break
        
        if not flag:
            answer = True
    
    return answer