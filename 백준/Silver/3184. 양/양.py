from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[0] * M for _ in range(N)]
cnt_o = 0
cnt_v = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] in 'ov' and not used[i][j]:
            used[i][j] = 1

            o = v = 0

            q = deque()
            q.append((i, j))

            while q:
                y, x = q.popleft()

                if lst[y][x] == 'o':
                    o += 1
                elif lst[y][x] == 'v':
                    v += 1

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != '#':
                        used[ny][nx] = 1
                        q.append((ny, nx))

            if o > v:
                cnt_o += o
            else:
                cnt_v += v


print(cnt_o, cnt_v)