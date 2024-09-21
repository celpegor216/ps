N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [[0] * M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if used[i][j]:
            continue
        
        result += 1

        q = [(i, j)]
        used[i][j] = 1

        while q:
            nq = []

            for y, x in q:
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and abs(lst[y][x] - lst[ny][nx]) <= K:
                        used[ny][nx] = 1
                        nq.append((ny, nx))
            
            q = nq

print(result)