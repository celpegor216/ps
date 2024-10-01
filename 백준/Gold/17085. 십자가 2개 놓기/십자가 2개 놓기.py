N, M = map(int, input().split())
lst = [input() for _ in range(N)]


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


result = 1
def dfs(level, start, used, total):
    global result

    if level == 2:
        result = max(result, total)
        return

    for n in range(start, N * M):
        i, j = n // M, n % M

        if lst[i][j] == '.' or used[i][j]:
            continue

        cnt = 1
        size = 1
        nxt_used = [line[:] for line in used]
        nxt_used[i][j] = 1
        while 1:
            dfs(level + 1, n + 1, [line[:] for line in nxt_used], total * cnt)

            flag = 0
            for dy, dx in directions:
                ny, nx = i + dy * size, j + dx * size
                if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx] or lst[ny][nx] == '.':
                    flag = 1
                    break
            if flag:
                break

            cnt += 4
            for dy, dx in directions:
                ny, nx = i + dy * size, j + dx * size
                nxt_used[ny][nx] = 1

            size += 1


dfs(0, 0, [[0] * M for _ in range(N)], 1)

print(result)