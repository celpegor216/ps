N = int(input())
lst = [input().split() for _ in range(N)]

positions = []
teachers = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'X':
            positions.append((i, j))
        elif lst[i][j] == 'T':
            teachers.append((i, j))

def check():
    for y, x in teachers:
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx

            while 0 <= ny < N and 0 <= nx < N:
                if lst[ny][nx] == 'S':
                    return 0
                elif lst[ny][nx] != 'X':
                    break
                ny += dy
                nx += dx
    return 1

M = len(positions)

def run():
    for i in range(M - 2):
        lst[positions[i][0]][positions[i][1]] = 'O'
        for j in range(i + 1, M - 1):
            lst[positions[j][0]][positions[j][1]] = 'O'
            for k in range(j + 1, M):
                lst[positions[k][0]][positions[k][1]] = 'O'
                if check():
                    return 'YES'
                lst[positions[k][0]][positions[k][1]] = 'X'
            lst[positions[j][0]][positions[j][1]] = 'X'
        lst[positions[i][0]][positions[i][1]] = 'X'

    return 'NO'

print(run())