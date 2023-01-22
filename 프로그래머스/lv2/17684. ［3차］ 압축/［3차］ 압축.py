def solution(msg):
    answer = []
    
    dic = {chr(ord('A') + x): x+1 for x in range(26)}
    
    last = 27
    start_idx = 0
    end_idx = 1
    length = len(msg)
    
    while end_idx < length:
        if msg[start_idx:end_idx + 1] in dic.keys():
            end_idx += 1
        else:
            answer.append(dic[msg[start_idx:end_idx]])
            dic[msg[start_idx:end_idx + 1]] = last
            last += 1
            start_idx = end_idx
            end_idx = start_idx + 1
    
    if start_idx < length:
        answer.append(dic[msg[start_idx:]])    
    
    return answer