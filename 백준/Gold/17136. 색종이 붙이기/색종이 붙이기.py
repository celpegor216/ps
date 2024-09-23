N = 10

lst = [list(map(int, input().split())) for _ in range(N)]

result = 26
papers = [0] * 6
used = [[0] * N for _ in range(N)]
def dfs(y, x, cnt):
    global result

    if cnt > result:
        return

    if y == N:
        result = cnt
        return

    ny, nx = y, x + 1
    if nx == N:
        ny += 1
        nx = 0

    if not lst[y][x] or used[y][x]:
        dfs(ny, nx, cnt)
    else:
        for i in range(1, 6):
            if papers[i - 1] == 5:
                continue

            if y + i > N or x + i > N:
                break

            flag = 0

            for dy in range(i):
                for dx in range(i):
                    if not lst[y + dy][x + dx] or used[y + dy][x + dx]:
                        flag = 1
                        break

                if flag:
                    break

            if flag:
                break

            papers[i - 1] += 1
            for dy in range(i):
                for dx in range(i):
                    used[y + dy][x + dx] = 1

            dfs(ny, nx, cnt + 1)

            papers[i - 1] -= 1
            for dy in range(i):
                for dx in range(i):
                    used[y + dy][x + dx] = 0

dfs(0, 0, 0)

print(result if result < 26 else -1)

