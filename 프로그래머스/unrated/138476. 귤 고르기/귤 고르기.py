def solution(k, tangerine):
    answer = 0
    
    dic = {}
    
    for t in tangerine:
        if t in dic.keys():
            dic[t] += 1
        else:
            dic[t] = 1
    
    lst = sorted(dic.values())
    
    total = 0
    while total < k:
        total += lst.pop()
        answer += 1
    
    return answer