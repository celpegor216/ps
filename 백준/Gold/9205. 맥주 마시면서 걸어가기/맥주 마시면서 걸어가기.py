from collections import deque

T = int(input())


MAX_DIST = 20 * 50
for _ in range(T):
    N = int(input())
    sy, sx = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    ey, ex = map(int, input().split())

    stores.sort(key=lambda x: abs(sy - x[0]) + abs(sx - x[1]))

    q = deque()
    q.append((sy, sx))

    used = [0] * N
    result = 'sad'

    while q:
        y, x = q.popleft()

        if abs(y - ey) + abs(x - ex) <= MAX_DIST:
            result = 'happy'
            break

        for n in range(N):
            if not used[n] and abs(y - stores[n][0]) + abs(x - stores[n][1]) <= MAX_DIST:
                q.append(stores[n])
                used[n] = 1

    print(result)