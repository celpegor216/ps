R, C = map(int, input().split())
lst = [input() for _ in range(R)]

result = 0
used = [[0] * C for _ in range(R)]
path = [0] * 26

def dfs(level, y, x):
    global result

    if level > result:
        result = level

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and not used[ny][nx] and not path[ord(lst[ny][nx]) - ord('A')]:
            used[ny][nx] = 1
            path[ord(lst[ny][nx]) - ord('A')] = 1
            dfs(level + 1, ny, nx)
            used[ny][nx] = 0
            path[ord(lst[ny][nx]) - ord('A')] = 0

used[0][0] = 1
path[ord(lst[0][0]) - ord('A')] = 1
dfs(1, 0, 0)

print(result)