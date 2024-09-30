# 디버깅 도움 받음



TC = int(input())

N, M = 5, 9


def dfs(level, now):
    global result

    result = max(result, level)

    if level == P - 1:
        return

    for i in range(N):
        for j in range(M):
            if now[i][j] != 'o':
                continue

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = i + dy, j + dx
                if not (0 <= ny < N and 0 <= nx < M) or now[ny][nx] != 'o':
                    continue

                nny, nnx = ny + dy, nx + dx
                if not (0 <= nny < N and 0 <= nnx < M) or now[nny][nnx] != '.':
                    continue

                nxt = [line[:] for line in now]
                nxt[i][j] = '.'

                nxt[ny][nx] = '.'
                nxt[nny][nnx] = 'o'

                dfs(level + 1, nxt)



for tc in range(TC):
    lst = [list(input()) for _ in range(N)]

    if tc != TC - 1:
        input()

    # 전체 핀의 수
    P = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'o':
                P += 1

    # 없앤 핀의 수
    result = 0
    dfs(0, lst)

    print(P - result, result)