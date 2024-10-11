N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        q = [(i, j)]
        used = [[0] * M for _ in range(N)]
        used[i][j] = 1

        min_max = 10001

        idx = 0
        while idx < len(q):
            y, x = q[idx]
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M):
                    q = []
                    break
                elif used[ny][nx]:
                    continue
                elif lst[ny][nx] > lst[i][j]:
                    min_max = min(min_max, lst[ny][nx])
                else:
                    used[ny][nx] = 1
                    q.append((ny, nx))
            idx += 1

        for y, x in q:
            result += min_max - lst[y][x]
            lst[y][x] = min_max

print(result)