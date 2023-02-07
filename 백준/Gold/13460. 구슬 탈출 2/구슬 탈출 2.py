# 해답: https://bgspro.tistory.com/70

from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

ry = rx = by = bx = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'R':
            ry, rx = i, j
        elif lst[i][j] == 'B':
            by, bx = i, j

def bfs(ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0))
    
    used = []
    used.append((ry, rx, by, bx, 0))
    
    while q:
        ry, rx, by, bx, cnt = q.popleft()
        
        if cnt == 11:
            print(-1)
            return
        
        if lst[ry][rx] == 'O':
            print(cnt)
            return

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            # 빨강 구슬 움직임
            nry, nrx = ry, rx
            
            while 1:
                nry += dy
                nrx += dx
                
                if lst[nry][nrx] == '#':
                    nry -= dy
                    nrx -= dx
                    break
                    
                if lst[nry][nrx] == 'O':
                    break
            
            # 파랑 구슬 움직임
            nby, nbx = by, bx
            
            while 1:
                nby += dy
                nbx += dx
                
                if lst[nby][nbx] == '#':
                    nby -= dy
                    nbx -= dx
                    break
                    
                if lst[nby][nbx] == 'O':
                    break
            
            # 파랑 구슬이 구멍에 들어간 경우 종료
            if lst[nby][nbx] == 'O':
                continue
            
            # 두 구슬이 이동한 위치가 같다면, 더 많이 이동한 구슬이 더 늦게 온 구슬이므로 한 칸 덜 이동
            if nry == nby and nrx == nbx:
                if abs(nry - ry) + abs(nrx - rx) > abs(nby - by) + abs(nbx - bx):
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx
            
            # 방문한 적 없는 위치라면 추가
            if (nry, nrx, nby, nbx, cnt + 1) not in used:
                q.append((nry, nrx, nby, nbx, cnt + 1))
                used.append((nry, nrx, nby, nbx, cnt + 1))

    print(-1)
    
bfs(ry, rx, by, bx)