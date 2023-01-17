def solution(number, limit, power):
    answer = 0
    
    bucket = [0] * (number + 1)
    
    for i in range(1, number + 1):
        j = 1
        while i * j <= number:
            bucket[i * j] += 1
            j += 1
    
    for i in range(1, number + 1):
        if bucket[i] <= limit:
            answer += bucket[i]
        else:
            answer += power
    
    return answer