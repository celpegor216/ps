from collections import deque

N, M, A, B, K = map(int, input().split())

lst = [[0] * (M + 1) for _ in range(N + 1)]

for k in range(K):
    y, x = map(int, input().split())
    lst[y][x] = -1

sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

q = deque()
q.append((sy, sx, 0))
lst[sy][sx] = 1

result = -1
while q:
    nowy, nowx, nowcnt = q.popleft()

    if nowy == ey and nowx == ex:
        result = nowcnt
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx

        if 1 <= ny <= N - A + 1 and 1 <= nx <= M - B + 1 and not lst[ny][nx]:
            flag = 0

            for i in range(A):
                if not flag:
                    for j in range(B):
                        if lst[ny + i][nx + j] == -1:
                            flag = 1
                            break
            
            if not flag:
                lst[ny][nx] = 1
                q.append((ny, nx, nowcnt + 1))

print(result)