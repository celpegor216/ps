def solution(intStrs, k, s, l):
    answer = []
    
    for item in intStrs:
        temp = int(item[s:s+l])
        if temp > k:
            answer.append(temp)
    
    return answer