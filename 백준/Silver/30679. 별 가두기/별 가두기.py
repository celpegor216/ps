N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

result = []
for n in range(N):
    y = n
    x = d = 0

    used = set()
    used.add((y, x, d))

    while 1:
        dy, dx = directions[d]
        y, x = y + dy * lst[y][x], x + dx * lst[y][x]
        d = (d + 1) % 4

        if not (0 <= y < N and 0 <= x < M):
            break

        if (y, x, d) not in used:
            used.add((y, x, d))
        else:
            result.append(n + 1)
            break

print(len(result))

if result:
    print(*result)