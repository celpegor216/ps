def solution(nums):
    bucket = [0] * 200001
    
    for num in nums:
        bucket[num] += 1
    
    N = len(nums) // 2
    
    cnt_one = 0
    for i in range(200001):
        if bucket[i] > 0:
            cnt_one += 1
    
    if cnt_one >= N:
        return N
    else:
        return cnt_one