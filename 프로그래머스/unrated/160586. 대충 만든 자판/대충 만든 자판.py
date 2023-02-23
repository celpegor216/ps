def solution(keymap, targets):
    answer = []
    
    bucket = [999] * 26
    
    for k in keymap:
        for i in range(len(k)):
            temp = ord(k[i]) - ord('A')
            if bucket[temp] > i + 1:
                bucket[temp] = i + 1
    
    for target in targets:
        total = 0
        
        for t in target:
            temp = ord(t) - ord('A')
            if bucket[temp] == 999:
                total = 0
                break
            total += bucket[temp]
        
        if total:
            answer.append(total)
        else:
            answer.append(-1)
    
    return answer