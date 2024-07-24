T = int(input())
N = 102

used = [[0] * N for _ in range(N)]

for _ in range(T):
    y, x = map(int, input().split())

    for i in range(10):
        for j in range(10):
            used[y + i][x + j] = 1

result = 0

for i in range(N):
    for j in range(N):
        if used[i][j]:
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = i + dy, j + dx

            if 0 <= ny < N and 0 <= nx < N and used[ny][nx]:
                result += 1

print(result)