from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    q = deque()
    q.append((sy, sx))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = 1

    result = 0

    while q:
        y, x = q.popleft()

        if y == ey and x == ex:
            result = used[y][x] - 1
            break

        for dy, dx in ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                q.append((ny, nx))
                used[ny][nx] = used[y][x] + 1

    print(result)