N = int(input())
lst = [list(input()) for _ in range(N)]

could_be_here = [[0] * N for _ in range(N)]
should_not_be_here = [[0] * N for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

for i in range(N):
    for j in range(N):
        if lst[i][j] == '.':
            continue

        elif lst[i][j] == 'X':
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '.':
                    could_be_here[ny][nx] = 1
                    ny += dy
                    nx += dx

        elif lst[i][j] == 'O':
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '.':
                    should_not_be_here[ny][nx] = 1
                    ny += dy
                    nx += dx

for i in range(N):
    for j in range(N):
        if lst[i][j] != '.':
            continue

        if not should_not_be_here[i][j] and could_be_here[i][j]:
            lst[i][j] = 'B'

for line in lst:
    print(''.join(line))