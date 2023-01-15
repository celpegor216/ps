def solution(s, n):
    answer = ''
    
    for i in s:
        if 'a' <= i <= 'z':
            temp = ord(i) - ord('a') + n
            
            if temp >= 26:
                temp %= 26
            
            answer += chr(ord('a') + temp)
        elif 'A' <= i <= 'Z':
            temp = ord(i) - ord('A') + n
            
            if temp >= 26:
                temp %= 26
            
            answer += chr(ord('A') + temp)
        else:
            answer += i
        
    
    return answer