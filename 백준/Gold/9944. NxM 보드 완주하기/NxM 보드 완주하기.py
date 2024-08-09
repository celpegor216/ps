tc = 0

while 1:
    try:
        tc += 1
        N, M = map(int, input().split())
        lst = [input() for _ in range(N)]

        result = 21e8
        used = [[0] * M for _ in range(N)]

        def dfs(level, y, x, left):
            global result

            if level >= result:
                return

            if not left:
                result = level
                return

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                nleft = left

                while 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '.':
                    used[ny][nx] = 1
                    ny += dy
                    nx += dx
                    nleft -= 1

                ny -= dy
                nx -= dx

                if not(ny == y and nx == x):
                    dfs(level + 1, ny, nx, nleft)

                while not(ny == y and nx == x):
                    used[ny][nx] = 0
                    ny -= dy
                    nx -= dx

        total = 0
        for i in range(N):
            for j in range(M):
                if lst[i][j] == '.':
                    total += 1

        for i in range(N):
            for j in range(M):
                if lst[i][j] == '.':
                    used[i][j] = 1
                    dfs(0, i, j, total - 1)
                    used[i][j] = 0

        print(f'Case {tc}: {result if result != 21e8 else -1}')
    except:
        break