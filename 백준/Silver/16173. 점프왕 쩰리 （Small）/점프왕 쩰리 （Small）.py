from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque()
q.append((0, 0))

used = [[0] * N for _ in range(N)]
used[0][0] = 1

result = 'Hing'
while q:
    y, x = q.popleft()

    if y == x == N - 1:
        result = 'HaruHaru'
        break

    for dy, dx in ((0, 1), (1, 0)):
        ny, nx = y + dy * lst[y][x], x + dx * lst[y][x]

        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
            q.append((ny, nx))
            used[ny][nx] = 1

print(result)