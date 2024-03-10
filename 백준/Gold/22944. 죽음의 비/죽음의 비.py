# bfs 구현인데 틀리는 이유를 모르겠음
# 해답: https://westmino.tistory.com/97

from collections import deque

N, H, D = map(int, input().split())
lst = [input() for _ in range(N)]

sy, sx = -1, -1

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'S':
            sy, sx = i, j

def bfs():
    q = deque()
    q.append((sy, sx, H, 0, 0))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = H

    while q:
        nowy, nowx, nowh, nowd, nowc = q.popleft()
        
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N:
                nh, nd, nc = nowh, nowd, nowc + 1

                if lst[ny][nx] == 'E':
                    return nc
                
                if lst[ny][nx] == 'U':
                    nd = D
                
                if nd:
                    nd -= 1
                else:
                    nh -= 1
                
                if used[ny][nx] < nh:
                    used[ny][nx] = nh
                    q.append((ny, nx, nh, nd, nc))

    return -1

print(bfs())