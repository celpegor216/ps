def solution(numbers):
    answer = 0
    N = len(numbers)
    
    max_v = int(''.join(sorted(list(numbers), reverse=True)))
    
    bucket = [0] * (max_v + 1)
    bucket[0] = 1
    bucket[1] = 1
    
    for i in range(2, max_v // 2 + 1):
        j = 2
        while i * j  <= max_v:
            bucket[i * j] = 1
            j += 1
    
    nums = set()
    used = [0] * N
    def dfs(level, path):
        if path:
            nums.add(int(path))
        
        if level == N:
            return
        
        for i in range(N):
            if not used[i]:
                used[i] = 1
                dfs(level + 1, path + numbers[i])
                used[i] = 0
    
    dfs(0, '')
    
    for num in nums:
        if not bucket[num]:
            answer += 1
    
    return answer