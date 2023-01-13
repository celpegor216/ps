def solution(array):
    answer = 0
    
    bucket = [0] * 1000
    
    for item in array:
        bucket[item] += 1
    
    max_v = 0
    max_c = 0
    cnt = 0

    for i in range(1000):
        if bucket[i] > max_c:
            max_v = i
            max_c = bucket[i]
            cnt = 1
        elif bucket[i] == max_c:
            cnt += 1
    
    if cnt > 1:
        answer = -1
    else:
        answer = max_v
    
    return answer