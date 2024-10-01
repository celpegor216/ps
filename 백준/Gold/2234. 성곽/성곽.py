M, N = map(int, input().split())
walls = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

groups = [[-1] * M for _ in range(N)]
groups_size = []
groups_idx = 0

for i in range(N):
    for j in range(M):
        if groups[i][j] != -1:
            continue

        groups[i][j] = groups_idx
        cnt = 1

        q = [(i, j)]

        while q:
            nq = []

            for y, x in q:
                for d in range(4):
                    if walls[y][x] & (1 << d):
                        continue

                    dy, dx = directions[d]
                    ny, nx = y + dy, x + dx

                    if groups[ny][nx] != -1:
                        continue

                    groups[ny][nx] = groups_idx
                    cnt += 1
                    nq.append((ny, nx))

            q = nq

        groups_idx += 1
        groups_size.append(cnt)


print(groups_idx)
print(max(groups_size))

max_cnt = 0
for i in range(N):
    for j in range(M):
        if i + 1 < N and groups[i][j] != groups[i + 1][j]:
            max_cnt = max(max_cnt, groups_size[groups[i][j]] + groups_size[groups[i + 1][j]])

        if j + 1 < M and groups[i][j] != groups[i][j + 1]:
            max_cnt = max(max_cnt, groups_size[groups[i][j]] + groups_size[groups[i][j + 1]])

print(max_cnt)