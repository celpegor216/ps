N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
oppo = {0: 1, 1: 0, 2: 3, 3: 2}
horses = []
used = [[[] for _ in range(N)] for _ in range(N)]

for k in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    used[y][x].append(k)
    horses.append([y, x, d])

result = -1

for t in range(1, 1001):
    for k in range(K):
        y, x, d = horses[k]

        ny, nx = y + directions[d][0], x + directions[d][1]

        if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
            d = oppo[d]
            horses[k][2] = d

            ny, nx = y + directions[d][0], x + directions[d][1]
            
        if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
            continue
        elif board[ny][nx] == 1:
            idx = used[y][x].index(k)

            for i in used[y][x][idx:]:
                horses[i][0] = ny
                horses[i][1] = nx
            used[ny][nx] += used[y][x][idx:][::-1]
            used[y][x] = used[y][x][:idx]
        else:
            idx = used[y][x].index(k)

            for i in used[y][x][idx:]:
                horses[i][0] = ny
                horses[i][1] = nx
            used[ny][nx] += used[y][x][idx:]
            used[y][x] = used[y][x][:idx]
        
        if len(used[ny][nx]) > 3:
            result = t
            break

    if result != -1:
        break

print(result)