def solution(s):
    answer = ''
    
    bucket = {}
    
    for i in s:
        if i in bucket.keys():
            bucket[i] += 1
        else:
            bucket[i] = 1
    
    for key in sorted(bucket.keys()):
        if bucket[key] == 1:
            answer += key
    
    return answer