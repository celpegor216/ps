def solution(s):
    answer = ''
    
    bucket = [0] * 256
    
    for i in s:
        bucket[ord(i)] += 1
    
    for i in range(255, -1, -1):
        answer += chr(i) * bucket[i]
    
    return answer