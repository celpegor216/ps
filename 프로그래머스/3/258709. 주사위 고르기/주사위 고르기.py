from collections import deque

def solution(dice):
    answer = []
    answer_cnt = 0
    
    N = len(dice)
    
    def check(lst):
        bucket = [0] * 501

        q = deque()
        q.append((0, 0))
        
        while q:
            total, level = q.popleft()

            if level == N // 2:
                bucket[total] += 1
                continue
            
            for item in dice[lst[level]]:
                q.append((total + item, level + 1))
        
        return bucket
    
    def dfs(level, start, lst):
        nonlocal answer_cnt, answer
        
        if level == N // 2:
            a = check(lst)
            b = check([x for x in range(N) if x not in lst])
            
            cnt = 0
            for i in range(1, 501):
                for j in range(1, i):
                    cnt += a[i] * b[j]
                    
            if cnt > answer_cnt:
                answer = lst[:]
                answer_cnt = cnt
            return

        for n in range(start, N):
            if n not in lst:
                dfs(level + 1, n + 1, lst + [n])
    
    dfs(0, 0, [])
    
    answer = [item + 1 for item in answer]
    
    return answer