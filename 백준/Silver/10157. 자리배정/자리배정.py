M, N = map(int, input().split())
K = int(input())

if K > M * N:
    print(0)
else:
    used = [[0] * M for _ in range(N)]

    y = N - 1
    x = 0
    d = 0
    k = 1

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while 1:
        used[y][x] = 1

        if k == K:
            print(x + 1, N - y)
            break

        dy, dx = directions[d]
        ny, nx = y + dy, x + dx
        
        if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx]:
            d = (d + 1) % 4
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx
        
        y, x = ny, nx
        k += 1