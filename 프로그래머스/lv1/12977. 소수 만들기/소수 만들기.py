def solution(nums):
    answer = 0
    
    memo = [0] * 50001
    
    for i in range(2, 25000):
        j = 2
        while i * j <= 50000:
            memo[i * j] = 1
            j += 1
    
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if not memo[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer