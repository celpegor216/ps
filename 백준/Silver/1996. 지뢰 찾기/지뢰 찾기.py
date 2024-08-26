N = int(input())
lst = [input() for _ in range(N)]

result = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j] == '.':
            continue

        num = int(lst[i][j])

        for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            ny, nx = i + dy, j + dx
            if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] != '*':
                result[ny][nx] += num

for i in range(N):
    for j in range(N):
        if lst[i][j] != '.':
            print('*', end='')
        elif result[i][j] > 9:
            print('M', end='')
        else:
            print(result[i][j], end='')
    print()