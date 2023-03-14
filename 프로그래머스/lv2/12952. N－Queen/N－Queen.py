# 상하 = level, 좌우 = lr, 좌하 = level - lr + n, 우상 = level + lr

def solution(n):
    answer = 0
    used_lr = [0] * n
    used_ld = [0] * (n * 2 + 1)
    used_ru = [0] * (n * 2 + 1)
    
    def dfs(level):
        nonlocal answer
        
        if level == n:
            answer += 1
            return
        
        for i in range(n):
            if not used_lr[i] and not used_ld[level - i + n] and not used_ru[level + i]:
                used_lr[i] = 1
                used_ld[level - i + n] = 1
                used_ru[level + i] = 1
                dfs(level + 1)
                used_lr[i] = 0
                used_ld[level - i + n] = 0
                used_ru[level + i] = 0
    
    dfs(0)
    
    return answer