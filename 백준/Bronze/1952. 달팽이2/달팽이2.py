N, M = map(int, input().split())

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

result = 0
y = x = d = 0
used = [[0] * M for _ in range(N)]
used[y][x] = 1

while 1:
    dy, dx = directions[d]
    ny, nx = y + dy, x + dx

    if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx]:
        d = (d + 1) % 4
        dy, dx = directions[d]
        ny, nx = y + dy, x + dx
        if used[ny][nx]:
            break
        result += 1
    
    used[ny][nx] = 1
    y, x = ny, nx

print(result)