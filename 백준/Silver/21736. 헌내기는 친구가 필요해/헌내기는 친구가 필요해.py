from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

sy, sx = -1, -1

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'I':
            sy = n
            sx = m

used = [[0] * M for _ in range(N)]
cnt = 0

q = deque()
q.append((sy, sx))
used[sy][sx] = 1

while q:
    nowy, nowx = q.popleft()

    if lst[nowy][nowx] == 'P':
        cnt += 1

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != 'X':
            used[ny][nx] = 1
            q.append((ny, nx))

if not cnt:
    print('TT')
else:
    print(cnt)