K = int(input())
N = 2 ** K

x, y = map(int, input().split())
x -= 1
y = N - y

ds = [((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0)), ((-1, 0), (0, 1))]

result = []

def dfs(level, now):
    if result:
        return

    if level == (N ** 2) // 3 + 1:
        flag = 0

        for line in now:
            if 0 in line:
                flag = 1
                break
        
        if not flag:
            for line in now:
                result.append(line[:])
        return

    for i in range(N):
        for j in range(N):
            if not now[i][j]:
                for a, b in ds:
                    x1, y1, x2, y2 = i + a[0], j + a[1], i + b[0], j + b[1]

                    if 0 <= x1 < N and 0 <= y1 < N and 0 <= x2 < N and 0 <= y2 < N and not now[x1][y1] and not now[x2][y2]:
                        tmp = [line[:] for line in now]
                        tmp[x1][y1] = level
                        tmp[x2][y2] = level
                        tmp[i][j] = level
                        dfs(level + 1, tmp)

lst = [[0] * N for _ in range(N)]
lst[y][x] = -1

dfs(1, lst)

if not result:
    print(-1)
else:
    for line in result:
        print(*line)