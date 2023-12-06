from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
H, W, sn, sm, en, em = map(int, input().split())

sn -= 1
sm -= 1
en -= 1
em -= 1

result = -1

used = [[0] * M for _ in range(N)]
q = deque()

for n in range(N):
    for m in range(M):
        if lst[n][m]:
            for h in range(H):
                for w in range(W):
                    nn, nm = n - h, m - w
                    if 0 <= nn < N and 0 <= nm < M:
                        used[nn][nm] = 1

used[sn][sm] = 1
q.append((sn, sm, 0))

while q:
    nowy, nowx, cnt = q.popleft()

    if nowy == en and nowx == em:
        result = cnt
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx

        if 0 <= ny < N and 0 <= nx < M and 0 <= ny + H - 1 < N and 0 <= nx + W - 1 < M and not used[ny][nx]:
            used[ny][nx] = 1
            q.append((ny, nx, cnt + 1))

print(result)