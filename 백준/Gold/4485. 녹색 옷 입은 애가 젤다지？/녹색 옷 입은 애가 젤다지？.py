from collections import deque

tc = 1
while 1:
    N = int(input())

    if N == 0:
        break

    lst = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    q.append((0, 0, lst[0][0]))

    used = [[21e8] * N for _ in range(N)]
    used[0][0] = lst[0][0]

    while q:
        y, x, c = q.popleft()

        if used[y][x] < c:
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and used[ny][nx] > c + lst[ny][nx]:
                used[ny][nx] = lst[ny][nx] + c
                q.append((ny, nx, c + lst[ny][nx]))

    print(f'Problem {tc}: {used[-1][-1]}')

    tc += 1