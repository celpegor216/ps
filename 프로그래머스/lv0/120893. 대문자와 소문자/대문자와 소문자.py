def solution(my_string):
    answer = ''
    
    for s in my_string:
        if 'a' <= s <= 'z':
            answer += chr(ord(s) - ord('a') + ord('A'))
        else:
            answer += chr(ord(s) + ord('a') - ord('A'))
    
    return answer