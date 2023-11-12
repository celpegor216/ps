from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

nq = deque()
wq = deque()
used = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'S':
            nq.append((n, m, 0))
            used[n][m] = 1
        if lst[n][m] == '*':
            wq.append((n, m))
            used[n][m] = 1

result = 'KAKTUS'

while nq:
    tmp_nq = deque()
    tmp_wq = deque()

    while wq:
        nowy, nowx = wq.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '.':
                used[ny][nx] = 1
                tmp_wq.append((ny, nx))

    wq = tmp_wq

    flag = 0
    while nq:
        nowy, nowx, nowc = nq.popleft()

        if lst[nowy][nowx] == 'D':
            flag = nowc
            break

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] in '.D':
                used[ny][nx] = 1
                tmp_nq.append((ny, nx, nowc + 1))
    
    nq = tmp_nq

    if flag:
        result = flag
        break

print(result)