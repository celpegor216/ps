from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
N = 4 * K
boards = [[list(input().strip()) for _ in range(N)]]

def check(y, x):
    return (y // 4) * K + x // 4

def turn(y, x):
    ty = x % 4 + (y - y % 4)
    tx = 3 - y % 4 + (x - x % 4)
    
    return ty, tx

for i in range(1, 4):
    boards.append([[''] * N for _ in range(N)])
    for n in range(N):
        for m in range(N):
            ty, tx = turn(n, m)
            boards[i][ty][tx] = boards[i - 1][n][m]

sy = sx = st = -1

for i in range(N):
    if sy != -1:
        break

    for j in range(N):
        if boards[0][i][j] == 'S':
            sy, sx = i, j
            st = check(sy, sx)
            break

q = deque()
q.append((sy, sx, 0, st, 0))    # y, x, 이동 횟수, 현재 영역, 현재 영역의 회전 횟수

used = [[[0] * N for _ in range(N)] for _ in range(4)]
used[0][sy][sx] = 1

result = -1
while q:
    nowy, nowx, nowc, nowt, nowd = q.popleft()

    if boards[nowd][nowy][nowx] == 'E':
        result = nowc
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < N:
            t = check(ny, nx)
            if t == nowt and boards[nowd][ny][nx] != '#':
                ty, tx = turn(ny, nx)

                nd = (nowd + 1) % 4
                
                if not used[nd][ty][tx]:                
                    used[nd][ty][tx] = 1
                    q.append((ty, tx, nowc + 1, t, nd))
            elif t != nowt and boards[0][ny][nx] != '#':
                ty, tx = turn(ny, nx)
                
                if not used[1][ty][tx]:                
                    used[1][ty][tx] = 1
                    q.append((ty, tx, nowc + 1, t, 1))

print(result)