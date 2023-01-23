def solution(k, dungeons):
    answer = 0
    length = len(dungeons)
    used = [0] * length
    
    def dfs(level, total):
        nonlocal answer
        
        if level == length:
            return
        
        for i in range(length):
            if not used[i] and dungeons[i][0] <= total:
                used[i] = 1
                if level + 1 > answer:
                    answer = level + 1
                dfs(level + 1, total - dungeons[i][1])
                used[i] = 0
    
    dfs(0, k)
    
    return answer