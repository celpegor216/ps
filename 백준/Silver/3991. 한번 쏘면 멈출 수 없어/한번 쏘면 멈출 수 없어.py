N, M, C = map(int, input().split())
colors = list(map(int, input().split()))

y = x = 0
result = [[0] * M for _ in range(N)]

direction = 1
for c in range(C):
    for _ in range(colors[c]):
        result[y][x] = c + 1
        x += direction
        if x == M:
            y += 1
            x -= 1
            direction *= -1
        elif x == -1:
            y += 1
            x += 1
            direction *= -1

for line in result:
    print(*line, sep='')