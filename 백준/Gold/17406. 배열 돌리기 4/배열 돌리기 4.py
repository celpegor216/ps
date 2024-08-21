N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
commands = []
for _ in range(K):
    y, x, dist = map(int, input().split())
    y -= 1
    x -= 1
    commands.append((y, x, dist))


result = 21e8
used = [0] * K
def dfs(level, lst):
    global result

    if level == K:
        for line in lst:
            result = min(result, sum(line))
        return

    for k in range(K):
        if not used[k]:
            used[k] = 1

            y, x, dist = commands[k]

            tmp = [line[:] for line in lst]

            for d in range(1, dist + 1):
                # 윗줄 왼쪽 > 오른쪽
                right_up = tmp[y - d][x + d]
                for i in range(x + d, x - d, -1):
                    tmp[y - d][i] = tmp[y - d][i - 1]

                # 오른쪽줄 위 > 아래
                right_down = tmp[y + d][x + d]
                for i in range(y + d, y - d + 1, -1):
                    tmp[i][x + d] = tmp[i - 1][x + d]
                tmp[y - d + 1][x + d] = right_up

                # 아랫줄 오른쪽 > 왼쪽
                left_down = tmp[y + d][x - d]
                for i in range(x - d, x + d - 1):
                    tmp[y + d][i] = tmp[y + d][i + 1]
                tmp[y + d][x + d - 1] = right_down

                # 왼쪽줄 아래 > 위
                for i in range(y - d, y + d - 1):
                    tmp[i][x - d] = tmp[i + 1][x - d]
                tmp[y + d - 1][x - d] = left_down

            dfs(level + 1, tmp)

            used[k] = 0

dfs(0, lst)

print(result)