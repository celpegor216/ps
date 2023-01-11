def solution(my_string):
    answer = []
    
    for s in my_string:
        if 'a' <= s <= 'z':
            answer.append(s)
        else:
            answer.append(chr(ord(s) - ord('A') + ord('a')))
    
    answer.sort()
    
    res = ''
    
    for s in answer:
        res += s
    
    return res