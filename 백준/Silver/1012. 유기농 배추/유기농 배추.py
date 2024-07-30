T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        lst[y][x] = 1

    result = 0
    used = [[0] * M for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if lst[n][m] and not used[n][m]:
                result += 1
                used[n][m] = 1
                stack = []
                now = (n, m)

                while 1:
                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = now[0] + dy, now[1] + dx

                        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] and not used[ny][nx]:
                            used[ny][nx] = 1
                            stack.append(now)
                            now = (ny, nx)
                            break
                    else:
                        if stack:
                            now = stack.pop()
                        else:
                            break

    print(result)
