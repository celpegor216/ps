# 반례 참고


N, M = map(int, input().split())
L, R = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]


def find():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2:
                return i, j


sy, sx = find()
q = [(sy, sx, 0, 0)]
used = [[L + R + 1] * M for _ in range(N)]
used[sy][sx] = 0

while q:
    nq = []

    for y, x, l, r in q:
        for dy, dx, dl, dr in ((0, 1, 0, 1), (1, 0, 0, 0), (0, -1, 1, 0), (-1, 0, 0, 0)):
            ny, nx, nl, nr = y + dy, x + dx, l + dl, r + dr
            if 0 <= ny < N and 0 <= nx < M and nl <= L and nr <= R and lst[ny][nx] != 1 and used[ny][nx] > nl + nr:
                used[ny][nx] = nl + nr
                nq.append((ny, nx, nl, nr))

    q = nq


result = 0
for i in range(N):
    for j in range(M):
        if used[i][j] <= L + R and lst[i][j] != 1:
            result += 1

print(result)