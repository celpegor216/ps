def solution(code):
    answer = ''
    
    mode = 0
    
    for i in range(len(code)):
        if not mode:
            if code[i] != '1':
                if not i % 2:
                    answer += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2:
                    answer += code[i]
            else:
                mode = 0    
    
    return answer if answer else 'EMPTY'