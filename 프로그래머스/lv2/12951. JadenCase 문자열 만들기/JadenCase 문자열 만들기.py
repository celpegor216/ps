def solution(s):
    answer = ''
    
    start = True
    
    for i in s:
        if i == ' ':
            answer += i
            start = True
        else:
            if start:
                if not '0' <= i <= '9':
                    answer += i.upper()
                else:
                    answer += i
                start = False
            else:
                if '0' <= i <= '9':
                    answer += i
                else:
                    answer += i.lower()
    
    return answer