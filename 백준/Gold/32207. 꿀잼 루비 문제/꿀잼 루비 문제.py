# 힌트: 그리디, 브루트포스, 백트래킹
# dp가 아 니 라 구???????????????????????????????????


N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

positions = dict()

for i in range(N):
    for j in range(M):
        if not positions.get(lst[i][j]):
            positions[lst[i][j]] = []
        positions[lst[i][j]].append((i, j))

positions = sorted(positions.items(), key=lambda x: (-x[0]))
used = []
length = len(positions)
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

found_all = length
result = 0
def dfs(level, nowy, nowx, total):
    global result, found_all

    result = max(result, total)

    if nowy >= found_all:
        return

    if level == K:
        found_all = nowy - 1
        return

    j = nowx
    for i in range(nowy, length):
        while j < len(positions[i][1]):
            y, x = positions[i][1][j]

            flag = 0
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and (ny, nx) in used:
                    flag = 1
                    break

            if not flag:
                used.append((y, x))
                dfs(level + 1, i, j + 1, total + positions[i][0])
                used.pop()

            if i >= found_all:
                return

            j += 1
        j = 0


dfs(0, 0, 0, 0)
print(result)