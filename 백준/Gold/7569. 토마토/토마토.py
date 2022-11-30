from collections import deque

M, N, H = map(int, input().split())

lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
used = [[[0] * M for _ in range(N)] for _ in range(H)]
result = 0

def bfs():
    global result

    q = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if lst[h][n][m] == 1:
                    q.append((h, n, m, 0))

    while q:
        nowh, nown, nowm, nowc = q.popleft()

        for dh, dn, dm in ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0), (1, 0, 0)):
            nh, nn, nm = nowh + dh, nown + dn, nowm + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not used[nh][nn][nm] \
                and lst[nh][nn][nm] == 0:
                used[nh][nn][nm] = 1
                q.append((nh, nn, nm, nowc + 1))
                if nowc + 1 > result:
                    result = nowc + 1

bfs()

for h in range(H):
    if result == -1:
        break
    for n in range(N):
        if result == -1:
            break
        for m in range(M):
            if lst[h][n][m] == 0 and used[h][n][m] == 0:
                result = -1
                break

print(result)