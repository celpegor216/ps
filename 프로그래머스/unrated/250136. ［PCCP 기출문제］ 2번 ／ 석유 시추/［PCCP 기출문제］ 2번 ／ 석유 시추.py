from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    used = [[0] * M for _ in range(N)]
    
    answer = [0] * M
    
    for n in range(N):
        for m in range(M):
            if not used[n][m] and land[n][m]:
                used[n][m] = 1
                q = deque()
                q.append((n, m))
                
                cols = set()
                cnt = 0
                
                while q:
                    y, x = q.popleft()
                    
                    cols.add(x)
                    cnt += 1
                    
                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and land[ny][nx]:
                            used[ny][nx] = 1
                            q.append((ny, nx))
                
                for col in cols:
                    answer[col] += cnt
    
    return max(answer)