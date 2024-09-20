N = int(input())

used = [(0, 0), (-2, 0)]

odd_directions = ((2, 0), (-1, -1), (-1, 1))
even_directions = ((-2, 0), (1, 1), (1, -1))

result = 0


def dfs(level, y, x, before_direction):
    global result

    if level == N + 1:
        return

    directions = odd_directions if level % 2 else even_directions
    for i in range(3):
        if i == before_direction:
            continue

        dy, dx = directions[i]
        ny, nx = y + dy, x + dx

        if (ny, nx) in used:
            if level == N:
                result += 1
        else:
            used.append((ny, nx))
            dfs(level + 1, ny, nx, i)
            used.pop()


if N >= 5:
    dfs(1, -2, 0, 0)

print(result)
