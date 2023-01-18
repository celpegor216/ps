# 2
# 2 3
# 2 2 2
# 2 7

def solution(arr):
    answer = 1
    
    bucket = [0] * 101
    
    for num in arr:
        temp = [0] * (num + 1)
        i = 2
        while num > 1:
            if not num % i:
                temp[i] += 1
                num //= i
            else:
                i += 1
        
        for i in range(2, len(temp)):
            bucket[i] = max(bucket[i], temp[i])
                
    for i in range(2, 101):
        answer *= i ** bucket[i]
    
    return answer