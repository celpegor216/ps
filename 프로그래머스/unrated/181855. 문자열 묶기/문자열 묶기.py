def solution(strArr):
    bucket = [0] * 31
    
    for s in strArr:
        bucket[len(s)] += 1
    
    answer = 0
    for i in range(31):
        if bucket[i] > answer:
            answer = bucket[i]

    return answer