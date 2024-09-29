N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

starts = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(3)]

used = [[[0] * 3 for _ in range(M)] for _ in range(N)]

def bfs(sy, sx, i):
    q = [(sy, sx)]
    used[sy][sx][i] = 1

    while q:
        nq = []

        for y, x in q:
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx][i] and not lst[ny][nx]:
                    used[ny][nx][i] = used[y][x][i] + 1
                    nq.append((ny, nx))

        q = nq

for i in range(3):
    bfs(starts[i][0], starts[i][1], i)

result = 21e8
result_cnt = 0
for i in range(N):
    for j in range(M):
        if 0 in used[i][j]:
            continue
        
        maxv = max(used[i][j])
        if maxv < result:
            result = maxv
            result_cnt = 1
        elif maxv == result:
            result_cnt += 1


if not result_cnt:
    print(-1)
else:
    print(result - 1)
    print(result_cnt)