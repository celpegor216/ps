def solution(n):
    answer = 0
    
    nums = []
    
    while n:
        nums.append(n % 10)
        n //= 10
    
    nums.sort()
    
    for i in range(len(nums)):
        answer += nums[i] * 10 ** i
    
    return answer