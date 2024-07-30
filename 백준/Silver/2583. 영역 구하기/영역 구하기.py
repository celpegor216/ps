N, M, K = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for _ in range(K):
    l, u, r, d = map(int, input().split())    # 주어진 영역을 가로축 기준 뒤집기

    for i in range(u, d):
        for j in range(l, r):
            lst[i][j] = 1

result = []
used = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if not lst[n][m] and not used[n][m]:
            total = 1
            used[n][m] = 1
            stack = []
            now = (n, m)

            while 1:
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = now[0] + dy, now[1] + dx

                    if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx]:
                        total += 1
                        used[ny][nx] = 1
                        stack.append(now)
                        now = (ny, nx)
                        break
                else:
                    if stack:
                        now = stack.pop()
                    else:
                        break
            result.append(total)

print(len(result))
print(*sorted(result))