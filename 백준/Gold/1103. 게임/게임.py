# 힌트: 그래프 탐색 + dp
# dp... 어떻게 적용해야하나...


import sys
sys.setrecursionlimit(10 ** 4)


N, M = map(int, input().split())
lst = []
for _ in range(N):
    S = input()
    tmp = []
    for s in S:
        if s.isdigit():
            tmp.append(int(s))
        else:
            tmp.append(s)
    lst.append(tmp)

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# memo[i][j]: (i, j)에서 갈 수 있는 최대 칸 수
memo = [[0] * M for _ in range(N)]

result = 0
used = [[0] * M for _ in range(N)]
def dfs(level, y, x):
    global result

    if not memo[y][x]:
        maxv = 0
        for dy, dx in directions:
            ny, nx = y + dy * lst[y][x], x + dx * lst[y][x]

            if not(0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == 'H':
                maxv = max(maxv, 1)
            elif used[ny][nx]:
                result = -1
                return - 1
            else:
                used[ny][nx] = 1
                tmp = dfs(level + 1, ny, nx)
                if tmp == -1:
                    return -1
                maxv = max(maxv, tmp + 1)
                used[ny][nx] = 0

        memo[y][x] = maxv

    return memo[y][x]

used[0][0] = 1
print(dfs(0, 0, 0))