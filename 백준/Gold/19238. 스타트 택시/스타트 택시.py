from collections import deque

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
customers = dict()
for _ in range(M):
    a, b, c, d = list(map(int, input().split()))
    customers[(a - 1, b - 1)] = (c - 1, d - 1)
    lst[a - 1][b - 1] = 2

flag = 0

for m in range(M):
    # 손님 찾기
    q = deque()
    q.append((sy, sx, 0))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = 1
    cy, cx, cc = N, N, N ** 2

    while q:
        nowy, nowx, nowc = q.popleft()

        if cc < nowc:
            continue

        if lst[nowy][nowx] == 2:
            if nowc < cc or (nowc == cc and (nowy < cy or (nowy == cy and nowx < cx))):
                cy = nowy
                cx = nowx
                cc = nowc
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] != 1:
                used[ny][nx] = 1
                q.append((ny, nx, nowc + 1))
    
    # 손님에게 이동
    K -= cc
    if K < 0 or cy == N:
        flag = 1
        break
    sy, sx = cy, cx
    lst[sy][sx] = 0

    # 목적지로 이동
    q = deque()
    q.append((sy, sx, 0))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = 1
    ty, tx = customers[(sy, sx)]
    move = -1

    while q:
        nowy, nowx, nowc = q.popleft()

        if nowy == ty and nowx == tx:
            move = nowc
            break

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] != 1:
                used[ny][nx] = 1
                q.append((ny, nx, nowc + 1))
    
    K -= move
    if K < 0 or move == -1:
        flag = 1
        break
    sy, sx = ty, tx
    K += move * 2

if flag:
    print(-1)
else:
    print(K)