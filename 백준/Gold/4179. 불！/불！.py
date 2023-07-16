# 힌트: 지훈이가 나중에 움직여야 함

from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

q = deque()
j = []
fs = []
result = 'IMPOSSIBLE'

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'J':
            j = f'J/{n}/{m}/0'
        elif lst[n][m] == 'F':
            fs.append(f'F/{n}/{m}/0')

for f in fs:
    q.append(f)
q.append(j)

while q:
    nowt, nowy, nowx, nowc = q.popleft().split('/')
    nowy = int(nowy)
    nowx = int(nowx)
    nowc = int(nowc)

    if nowt == 'J' and (nowy in (0, N - 1) or nowx in (0, M - 1)):
        result = nowc + 1
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != '#':
            if (nowt == 'J' and lst[ny][nx] == '.') or (nowt == 'F' and lst[ny][nx] != 'F'):
                lst[ny][nx] = nowt
                q.append(f'{nowt}/{ny}/{nx}/{nowc + 1}')

print(result)