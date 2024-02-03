N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dots = set()

for x, y, d, g in curves:
    tmp = [(x, y), (x + directions[d][0], y + directions[d][1])]

    for _ in range(g):
        nx, ny = tmp[-1]

        for i in range(len(tmp) - 2, -1, -1):
            nx += tmp[i + 1][1] - tmp[i][1]
            ny += tmp[i][0] - tmp[i + 1][0]
            tmp.append((nx, ny))
    
    for dot in tmp:
        dots.add(dot)

result = 0

for i in range(100):
    for j in range(100):
        flag = 0

        for dx, dy in ((0, 0), (0, 1), (1, 1), (1, 0)):
            if (i + dx, j + dy) not in dots:
                flag = 1
                break
                
        if not flag:
            result += 1

print(result)