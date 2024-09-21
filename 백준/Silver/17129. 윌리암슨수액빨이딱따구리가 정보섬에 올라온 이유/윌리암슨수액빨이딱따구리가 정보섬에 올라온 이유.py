N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

def find_position():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2:
                return i, j


def find():
    sy, sx = find_position()

    q = []
    q.append((sy, sx))

    used = [[0] * M for _ in range(N)]
    used[sy][sx] = 1

    result = 0
    while q:
        nq = []

        for y, x in q:
            if lst[y][x] > 2:
                return 'TAK', result

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != 1:
                    nq.append((ny, nx))
                    used[ny][nx] = 1
        
        q = nq
        result += 1
    
    return 'NIE', -1

res, cnt = find()

print(res)
if cnt > -1:
    print(cnt)