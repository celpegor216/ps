N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

groups = []

used = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if used[i][j]:
            continue

        q = [(i, j)]
        used[i][j] = 1

        idx = 0
        while idx < len(q):
            y, x = q[idx]
            for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if lst[y][x] == lst[ny][nx] and not used[ny][nx]:
                        q.append((ny, nx))
                        used[ny][nx] = 1
                    elif lst[y][x] < lst[ny][nx]:
                        used[y][x] = 2
            idx += 1

        groups.append(q)

result = 0

for group in groups:
    for y, x in group:
        if used[y][x] == 2:
            break
    else:
        result += 1
print(result)