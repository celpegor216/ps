from collections import deque

def solution(maps):
    answer = -1
    
    q = deque()
    q.append((0, 0, 1))
    
    N, M = len(maps), len(maps[0])
    
    used = [[0] * M for _ in range(N)]
    used[0][0] = 1
    
    while q:
        nowy, nowx, nowc = q.popleft()
        
        if nowy == N - 1 and nowx == M - 1:
            answer = nowc
            break
            
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and maps[ny][nx] == 1:
                q.append((ny, nx, nowc + 1))
                used[ny][nx] = 1
    
    return answer