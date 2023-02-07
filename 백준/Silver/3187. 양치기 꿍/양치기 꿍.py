from collections import deque

R, C = map(int, input().split())
lst = [input() for _ in range(R)]

sheeps = wolves = 0

used = [[0] * C for _ in range(R)]

def bfs(y, x):
    global sheeps, wolves

    q = deque()
    q.append((y, x))

    used[y][x] = 1

    s = w = 0

    if lst[y][x] == 'v':
        w += 1
    elif lst[y][x] == 'k':
        s += 1

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < R and 0 <= nx < C and not used[ny][nx] and lst[ny][nx] != '#':
                q.append((ny, nx))
                used[ny][nx] = 1

                if lst[ny][nx] == 'v':
                    w += 1
                elif lst[ny][nx] == 'k':
                    s += 1

    if s > w:
        sheeps += s
    else:
        wolves += w

for r in range(R):
    for c in range(C):
        if lst[r][c] != '#' and not used[r][c]:
            bfs(r, c)

print(sheeps, wolves)