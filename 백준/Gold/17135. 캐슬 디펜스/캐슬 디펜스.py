from collections import deque

N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for n in range(N):
    for m in range(M):
        cnt += lst[n][m]

result = 0

for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            total = 0
            c = cnt
            board = [line[:] for line in lst]
            X = [i, j, k]

            while c:
                attack = [[] for _ in range(3)]

                for l in range(3):
                    q = deque()
                    q.append((N, X[l], 0))
                    used = [[0] * M for _ in range(N)]

                    while q:
                        nowy, nowx, nowd = q.popleft()

                        if nowd > D or (attack[l] and nowd > attack[l][2]):
                            break

                        if 0 <= nowy < N and 0 <= nowx < M and board[nowy][nowx]:
                            if not attack[l] or (attack[l] and attack[l][1] > nowx):
                                attack[l] = [nowy, nowx, nowd]
                            continue

                        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            ny, nx = nowy + dy, nowx + dx
                            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                                used[ny][nx] = 1
                                q.append((ny, nx, nowd + 1))
                
                for a in attack:
                    if a:
                        y, x, d = a
                        if board[y][x]:
                            c -= 1
                            total += 1
                            board[y][x] = 0
                
                for m in range(M):
                    c -= board[-1][m]
                
                new_board = [[0] * M for _ in range(N)]

                for n in range(1, N):
                    new_board[n] = board[n - 1][:]
                
                board = new_board

            result = max(result, total)

print(result)