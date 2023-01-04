from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(M)]

white = 0
blue = 0

used = [[0] * N for _ in range(M)]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    color = lst[y][x]
    cnt = 1

    used[y][x] = 1

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < M and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] == color:
                q.append((ny, nx))
                cnt += 1
                used[ny][nx] = 1

    return cnt ** 2

for m in range(M):
    for n in range(N):
        if not used[m][n]:
            cnt = bfs(m, n)

            if lst[m][n] == 'W':
                white += cnt
            else:
                blue += cnt

print(white, blue)