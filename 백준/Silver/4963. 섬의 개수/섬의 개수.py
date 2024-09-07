from collections import deque

directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

while 1:
    M, N = map(int, input().split())

    if N == M == 0:
        break
    
    lst = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    used = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not lst[i][j] or used[i][j]:
                continue

            result += 1
            used[i][j] = 1

            q = deque()
            q.append((i, j))
            
            while q:
                y, x = q.popleft()
                
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] and not used[ny][nx]:
                        used[ny][nx] = 1
                        q.append((ny, nx))
    
    print(result)