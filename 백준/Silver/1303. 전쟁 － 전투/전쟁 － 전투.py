M, N = map(int, input().split())
lst = [input() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

W = B = 0
used = [[0] * M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if used[i][j]:
            continue
        
        q = [(i, j)]
        used[i][j] = 1
        cnt = 1

        while q:
            nq = []

            for y, x in q:
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == lst[i][j]:
                        used[ny][nx] = 1
                        cnt += 1
                        nq.append((ny, nx))
            
            q = nq

        if lst[i][j] == 'W':
            W += cnt ** 2
        else:
            B += cnt ** 2


print(W, B)