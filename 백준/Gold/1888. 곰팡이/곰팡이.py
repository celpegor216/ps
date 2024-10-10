N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

def grouping():
    used = [[0] * M for _ in range(N)]

    groups = []

    for i in range(N):
        for j in range(M):
            if not lst[i][j] or used[i][j]:
                continue

            used[i][j] = 1
            q = [(i, j)]
            idx = 0

            while idx < len(q):
                y, x = q[idx]
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                        used[ny][nx] = 1
                        q.append((ny, nx))

                idx += 1

            groups.append(q)

    return groups


result = 0
while 1:
    # 한 덩어리인지 확인
    groups = grouping()

    if len(groups) == 1:
        print(result)
        break

    # 곰팡이 번식
    new_lst = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not lst[i][j]:
                continue

            ranges = range(-lst[i][j], lst[i][j] + 1)

            for a in ranges:
                for b in ranges:
                    ny, nx = i + a, j + b
                    if 0 <= ny < N and 0 <= nx < M:
                        new_lst[ny][nx] = max(new_lst[ny][nx], lst[i][j])

    lst = new_lst
    result += 1