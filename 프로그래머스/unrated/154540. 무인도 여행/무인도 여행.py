from collections import deque

def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    
    used = [[0] * M for _ in range(N)]

    def bfs(y, x):
        nonlocal answer
        
        q = deque()
        q.append((y, x))
        
        used[y][x] = 1
        
        total = int(maps[y][x])
        
        while q:
            nowy, nowx = q.popleft()
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = nowy + dy, nowx + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and maps[ny][nx] != 'X':
                    total += int(maps[ny][nx])
                    used[ny][nx] = 1
                    q.append((ny, nx))
        
        answer.append(total)
    
    for n in range(N):
        for m in range(M):
            if not used[n][m] and maps[n][m] != 'X':
                bfs(n, m)

    return sorted(answer) if answer else [-1]