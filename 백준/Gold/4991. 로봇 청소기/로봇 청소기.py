directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(si, sj):
    q = [(si, sj)]
    used = [[21e8] * M for _ in range(N)]
    used[si][sj] = 0

    while q:
        nq = []

        for y, x in q:
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and used[ny][nx] == 21e8 and lst[ny][nx] != 'x':
                    used[ny][nx] = used[y][x] + 1
                    nq.append((ny, nx))

        q = nq

    return used


def dfs(level, now, total):
    global result

    if total >= result:
        return

    if level == K:
        result = min(result, total)
        return

    for k in range(K):
        if not used[k]:
            used[k] = 1
            dfs(level + 1, k, total + distances_between_dusts[now][k])
            used[k] = 0


while 1:
    M, N = map(int, input().split())

    if M == 0:
        break

    sy = sx = -1
    dusts = []
    lst = []
    for n in range(N):
        tmp = input()
        for m in range(M):
            if tmp[m] == '*':
                dusts.append((n, m))
            elif tmp[m] == 'o':
                sy, sx = n, m
        lst.append(tmp)

    K = len(dusts)

    distances_from_start_to_dusts = [21e8] * K
    used = bfs(sy, sx)
    for k in range(K):
        y, x = dusts[k]
        distances_from_start_to_dusts[k] = used[y][x]

    distances_between_dusts = [[21e8] * K for _ in range(K)]
    for a in range(K - 1):
        used = bfs(*dusts[a])
        for b in range(a + 1, K):
            y, x = dusts[b]
            distances_between_dusts[a][b] = used[y][x]
            distances_between_dusts[b][a] = used[y][x]

    result = 21e8
    used = [0] * K
    for k in range(K):
        used[k] = 1
        dfs(1, k, distances_from_start_to_dusts[k])
        used[k] = 0

    print(result if result != 21e8 else -1)