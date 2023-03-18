from collections import deque

def solution(maps):
    answer = -1
    N = len(maps)
    M = len(maps[0])
        
    def bfs(y, x, target):
        q = deque()
        used = [[0] * M for _ in range(N)]
        
        q.append((y, x, 0))
        used[y][x] = 1
        
        while q:
            nowy, nowx, nowc = q.popleft()
            
            if maps[nowy][nowx] == target:
                return (nowy, nowx, nowc)
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = nowy + dy, nowx + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and maps[ny][nx] != 'X':
                    q.append((ny, nx, nowc + 1))
                    used[ny][nx] = 1
    
    for i in range(N):
        for j in range(M):
            # 시작부터 레버까지
            if maps[i][j] == 'S':
                result = bfs(i, j, 'L')
                
                if result:
                    temp = bfs(result[0], result[1], 'E')
                    
                    if temp:
                        answer = result[2] + temp[2]
    
    return answer