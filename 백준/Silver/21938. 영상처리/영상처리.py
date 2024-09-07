from collections import deque

N, M = map(int, input().split())
lst = [[0] * M for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(N)]
T = int(input()) * 3

for i in range(N):
    for j in range(M):
        for k in range(3):
            lst[i][j] += inputs[i][j * 3 + k]
        if lst[i][j] >= T:
            lst[i][j] = 255
        else:
            lst[i][j] = 0

result = 0
used = [[0] * M for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

for i in range(N):
    for j in range(M):
        if used[i][j] or not lst[i][j]:
            continue

        result += 1

        used[i][j] = 1

        q = deque()
        q.append((i, j))

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                    used[ny][nx] = 1
                    q.append((ny, nx))

print(result)