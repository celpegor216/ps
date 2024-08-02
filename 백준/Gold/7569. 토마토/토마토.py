from collections import deque

M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
used = [[[0] * M for _ in range(N)] for _ in range(H)]

cnt = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 1:
                q.append((i, j, k))
                used[i][j][k] = 1
            elif not lst[i][j][k]:
                cnt += 1

while q:
    i, j, k = q.popleft()

    for di, dj, dk in ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
        ni, nj, nk = i + di, j + dj, k + dk

        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not used[ni][nj][nk] and not lst[ni][nj][nk]:
            cnt -= 1
            q.append((ni, nj, nk))
            used[ni][nj][nk] = used[i][j][k] + 1

if cnt:
    print(-1)
else:
    print(used[i][j][k] - 1)