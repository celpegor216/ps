def solution(n):
    answer = 0
    
    nums = [x for x in range(n + 1)]
    
    for i in range(2, n + 1):
        j = 2
        while i * j <= n:
            nums[i * j] = -1
            j += 1
    
    for i in range(1, n + 1):
        if nums[i] == -1:
            answer += 1
    
    return answer