def solution(s, skip, index):
    answer = ''
    
    for i in s:
        cnt = 0
        idx = 0
        while cnt < index:
            idx += 1
            if chr((ord(i) - ord('a') + idx) % 26 + ord('a')) not in skip:
                cnt += 1
        answer += chr((ord(i) - ord('a') + idx) % 26 + ord('a'))
    
    return answer