N, *percentages = list(map(int, input().split()))

for i in range(4):
    percentages[i] /= 100
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

used = [(0, 0)]
result = 0
def dfs(level, y, x, total):
    global result

    if level == N:
        result += total
        return

    for i in range(4):
        dy, dx = directions[i]
        ny, nx = y + dy, x + dx
        if (ny, nx) in used:
            continue

        used.append((ny, nx))
        dfs(level + 1, ny, nx, total * percentages[i])
        used.pop()

dfs(0, 0, 0, 1)

print(result)