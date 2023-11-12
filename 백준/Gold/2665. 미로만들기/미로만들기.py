from collections import deque

N = int(input())
lst = [input() for _ in range(N)]

q = deque()
used = [[[21e8, 21e8] for _ in range(N)] for _ in range(N)]

q.append((0, 0, 0)) # y, x, cnt

while q:
    nowy, nowx, nowc = q.popleft()

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < N:
            if lst[ny][nx] == '1':
                if used[ny][nx][0] > nowc:
                    used[ny][nx][0] = nowc
                    q.append((ny, nx, nowc))
            else:
                if used[ny][nx][1] > nowc + 1:
                    used[ny][nx][1] = nowc + 1
                    q.append((ny, nx, nowc + 1))

print(min(used[-1][-1]))