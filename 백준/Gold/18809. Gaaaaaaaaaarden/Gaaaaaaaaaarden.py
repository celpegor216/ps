# 시간초과
# 해답: https://westmino.tistory.com/44

import sys
input = sys.stdin.readline

from collections import deque

N, M, G, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

candidates = []
for n in range(N):
    for m in range(M):
        if lst[n][m] == 2:
            candidates.append((n, m))

length = len(candidates)
used_candidates = [0] * length

result = 0
MAXV = 21e8

def bfs():
    global result

    res = 0
    q = deque()
    used = [[0] * M for _ in range(N)]

    for i in range(length):
        if not used_candidates[i]:
            continue
        y, x = candidates[i]
        q.append((y, x, used_candidates[i], 1))
        used[y][x] = used_candidates[i]

    while q:
        y, x, t, c = q.popleft()

        if used[y][x] == MAXV:
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and used[ny][nx] != MAXV and lst[ny][nx]:
                if not used[ny][nx]:
                    used[ny][nx] = t * (c + 1)
                    q.append((ny, nx, t, c + 1))
                elif used[ny][nx] * -1 == t * (c + 1):
                    used[ny][nx] = MAXV
                    res += 1
    
    result = max(result, res)


def dfs(level, start, t):
    if level == G + R:
        bfs()
        return

    for i in range(start, length):
        if not used_candidates[i]:
            used_candidates[i] = t

            if level + 1 == G:
                dfs(level + 1, 0, -1)
            else:
                dfs(level + 1, i + 1, t)

            used_candidates[i] = 0

dfs(0, 0, 1)

print(result)