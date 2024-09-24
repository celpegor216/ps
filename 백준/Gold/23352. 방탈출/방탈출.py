N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

max_path_cnt = -1
max_password = -1
for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            continue

        q = [(i, j)]
        used = [[0] * M for _ in range(N)]
        used[i][j] = 1

        while q:
            nq = []

            for y, x in q:
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                        used[ny][nx] = used[y][x] + 1
                        q.append((ny, nx))

            q = nq

        path_cnt = used[y][x]
        password = lst[i][j] + lst[y][x]

        if path_cnt == 1:
            continue

        if max_path_cnt < path_cnt or (max_path_cnt == path_cnt and max_password < password):
            max_path_cnt = path_cnt
            max_password = password

print(max_password if max_password > 0 else 0)
