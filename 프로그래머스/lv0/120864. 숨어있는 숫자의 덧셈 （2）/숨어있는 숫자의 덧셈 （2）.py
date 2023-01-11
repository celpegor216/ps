def solution(my_string):
    answer = 0
    
    temp = '0'
    
    for s in my_string:
        if '0' <= s <= '9':
            temp += s
        else:
            answer += int(temp)
            temp = '0'
    
    if temp != '0':
        answer += int(temp)
    
    return answer