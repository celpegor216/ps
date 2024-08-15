from collections import deque

def find_start():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if lst[i][j][k] == 'S':
                    return i, j, k

while 1:
    H, N, M = map(int, input().split())

    if H == 0:
        break

    lst = []

    for i in range(H):
        tmp = [input() for _ in range(N)]
        _ = input()
        lst.append(tmp)

    q = deque()
    used = [[[0] * M for _ in range(N)] for _ in range(H)]
    
    i, j, k = find_start()
    q.append((i, j, k))
    used[i][j][k] = 1

    result = 0
    while q:
        z, y, x = q.popleft()

        if lst[z][y][x] == 'E':
            result = used[z][y][x] - 1
            break

        for dz, dy, dx in ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)):
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and not used[nz][ny][nx] and lst[nz][ny][nx] != '#':
                used[nz][ny][nx] = used[z][y][x] + 1
                q.append((nz, ny, nx))
    
    print(f'Escaped in {result} minute(s).' if result else 'Trapped!')