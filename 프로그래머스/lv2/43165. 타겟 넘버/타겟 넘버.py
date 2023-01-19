def solution(numbers, target):
    answer = 0
    
    N = len(numbers)
    used = ['+'] * N
    
    def dfs(level):
        nonlocal answer
        
        if level == N:
            total = 0
            for n in range(N):
                if used[n] == '+':
                    total += numbers[n]
                else:
                    total -= numbers[n]
            if total == target:
                answer += 1
            return
        
        dfs(level + 1)
        used[level] = '-'
        dfs(level + 1)
        used[level] = '+'
        
    
    dfs(0)
    
    return answer