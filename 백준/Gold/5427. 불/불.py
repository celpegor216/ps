from collections import deque

T = int(input())

for t in range(T):
    M, N = map(int, input().split())
    lst = [input() for _ in range(N)]

    sy = sx = -1
    fire = []

    for n in range(N):
        for m in range(M):
            if lst[n][m] == '@':
                sy = n
                sx = m
            elif lst[n][m] == '*':
                fire.append((n, m))
    
    used = [[[0, 0] for _ in range(M)] for _ in range(N)]

    q = deque()
    for y, x in fire:
        q.append((y, x, 0, 0))
        used[y][x][0] = 1
    q.append((sy, sx, 1, 0))
    used[sy][sx][1] = 1

    result = -1

    while q and result == -1:
        nowy, nowx, nowt, nowc = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if nowt == 0:
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx][nowt] and lst[ny][nx] != '#':
                    used[ny][nx][nowt] = 1
                    q.append((ny, nx, nowt, nowc + 1))
            else:
                if 0 <= ny < N and 0 <= nx < M and not sum(used[ny][nx]) and lst[ny][nx] != '#':
                    used[ny][nx][nowt] = 1
                    q.append((ny, nx, nowt, nowc + 1))
                elif not (0 <= ny < N and 0 <= nx < M):
                    result = nowc + 1
                    break
    
    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)
