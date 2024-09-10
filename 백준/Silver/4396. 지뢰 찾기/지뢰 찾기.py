N = int(input())
lst = [input() for _ in range(N)]
opened = [input() for _ in range(N)]

directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def check():
    for i in range(N):
        for j in range(N):
            if opened[i][j] == 'x' and lst[i][j] == '*':
                return 1
    return 0


bombed = check()

for i in range(N):
    for j in range(N):
        if bombed and lst[i][j] == '*':
            print('*', end='')
            continue

        if opened[i][j] == '.':
            print('.', end='')
            continue

        cnt = 0
        for dy, dx in directions:
            ny, nx = i + dy, j + dx
            if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '*':
                cnt += 1
        print(cnt, end='')
    print()
