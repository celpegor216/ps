from collections import deque

M, N = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[[21e8, 21e8] for _ in range(M)] for _ in range(N)]
used[0][0] = [0, 0]

q = deque()
q.append((0, 0, 0))

while q:
    y, x, cnt = q.popleft()

    if y == N - 1 and x == M - 1:
        continue

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == '0' and used[ny][nx][0] > cnt:
                used[ny][nx][0] = cnt
                q.append((ny, nx, cnt))
            elif lst[ny][nx] == '1' and used[ny][nx][1] > cnt + 1:
                used[ny][nx][1] = cnt + 1
                q.append((ny, nx, cnt + 1))

print(min(used[-1][-1]))