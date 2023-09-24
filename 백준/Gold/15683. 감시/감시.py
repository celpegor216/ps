N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cctvs = []

cnt = 0
for n in range(N):
    for m in range(M):
        if 0 < lst[n][m] < 6:
            cctvs.append([n, m, lst[n][m], -1])
        elif lst[n][m] == 0:
            cnt += 1

length = len(cctvs)

result = cnt

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(level):
    global result, cnt
    if level == length:
        # 사각 지대 개수 세기
        total = cnt

        used = [[0] * M for _ in range(N)]

        for i in range(length):
            y, x, num, d = cctvs[i]
            if num == 1:
                ny, nx = y + ds[d][0], x + ds[d][1]
                while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                    used[ny][nx] = 1
                    ny += ds[d][0]
                    nx += ds[d][1]
            elif num == 2:
                for j in range(2):
                    td = d + j * 2
                    ny, nx = y + ds[td][0], x + ds[td][1]
                    while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                        used[ny][nx] = 1
                        ny += ds[td][0]
                        nx += ds[td][1]
            elif num == 3:
                for j in range(2):
                    td = (d + j) % 4
                    ny, nx = y + ds[td][0], x + ds[td][1]
                    while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                        used[ny][nx] = 1
                        ny += ds[td][0]
                        nx += ds[td][1]
            elif num == 4:
                for j in range(3):
                    td = (d + j) % 4
                    ny, nx = y + ds[td][0], x + ds[td][1]
                    while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                        used[ny][nx] = 1
                        ny += ds[td][0]
                        nx += ds[td][1]
            else:
                for td in range(4):
                    ny, nx = y + ds[td][0], x + ds[td][1]
                    while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                        used[ny][nx] = 1
                        ny += ds[td][0]
                        nx += ds[td][1]

        for n in range(N):
            for m in range(M):
                if used[n][m] == 1 and lst[n][m] == 0:
                    total -= 1

        result = min(result, total)
        return

    if cctvs[level][2] == 2:
        for i in range(2):
            cctvs[level][3] = i
            dfs(level + 1)
    elif cctvs[level][2] != 5:
        for i in range(4):
            cctvs[level][3] = i
            dfs(level + 1)
    else:
        dfs(level + 1)

dfs(0)

print(result)