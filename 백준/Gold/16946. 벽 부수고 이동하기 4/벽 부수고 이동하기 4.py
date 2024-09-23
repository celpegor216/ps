N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

groups = [[-1] * M for _ in range(N)]
groups_cnt = []
groups_idx = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] != 0 or groups[i][j] != -1:
            continue

        cnt = 1
        groups[i][j] = groups_idx
        q = [(i, j)]

        while q:
            nq = []

            for y, x in q:
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and groups[ny][nx] == -1:
                        groups[ny][nx] = groups_idx
                        nq.append((ny, nx))
                        cnt += 1

            q = nq

        groups_cnt.append(cnt)
        groups_idx += 1


for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            print(lst[i][j], end='')
        else:
            possibles = set()
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx]:
                    possibles.add(groups[ny][nx])
            print((sum([groups_cnt[item] for item in possibles]) + 1) % 10, end='')

    print()