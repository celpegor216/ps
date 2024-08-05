from collections import deque

N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [0] * M
result = 0

def dfs(start, level, positions):
    global result

    if level == 3:
        total_attack = set()

        for n in range(N):
            attack = set()

            for pos in positions:
                q = deque()
                q.append((N - n - 1, pos))

                tmp_used = [[0] * M for _ in range(N)]
                tmp_used[N - n - 1][pos] = 1

                ry = N
                rx = M
                rc = D

                while q:
                    y, x = q.popleft()

                    if tmp_used[y][x] > rc:
                        break

                    if lst[y][x] == 1 and (y, x) not in total_attack:
                        if tmp_used[y][x] < rc:
                            ry = y
                            rx = x
                            rc = tmp_used[y][x]
                        elif tmp_used[y][x] == rc and rx > x:
                            ry = y
                            rx = x
                        else:
                            continue

                    for dy, dx in ((0, 1), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N - n and 0 <= nx < M and not tmp_used[ny][nx] and (ny, nx) not in total_attack:
                            tmp_used[ny][nx] = tmp_used[y][x] + 1
                            q.append((ny, nx))

                if 0 <= ry < N - n and 0 <= rx < M:
                    attack.add((ry, rx))

            total_attack = total_attack.union(attack)
        result = max(result, len(total_attack))
        return

    for i in range(start + 1, M):
        if not used[i]:
            used[i] = 1
            dfs(i, level + 1, positions + [i])
            used[i] = 0

dfs(-1, 0, [])

print(result)