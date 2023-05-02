# 시간 초과 해결 힌트: dp 추가해야 함

from collections import deque

def solution(board):
    answer = 21e8
    N = len(board)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    used = [[[21e8] * 4 for _ in range(N)] for _ in range(N)]
    for i in range(4):
        used[0][0][i] = 0
    
    q = deque()
    q.append((0, 0, 0, 0))
    q.append((0, 0, 1, 0))
    
    while q:
        nowy, nowx, nowd, total = q.popleft()
        
        if total >= answer:
            continue
        
        if nowy == nowx == N - 1:
            answer = total
            continue
        
        for i in range(4):
            ny, nx = nowy + d[i][0], nowx + d[i][1]
            
            if 0 <= ny < N and 0 <= nx < N and not board[ny][nx]:
                if nowd == i:
                    temp = total + 100
                else:
                    temp = total + 600
                
                if used[ny][nx][i] > temp:
                    used[ny][nx][i] = temp
                    q.append((ny, nx, i, temp))
    
    return answer