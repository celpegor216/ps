N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

def find():
    global N, M, lst

    for n in range(N):
        for m in range(M):
            if lst[n][m] == 'W':
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = n + dy, m + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        if lst[ny][nx] == 'S':
                            return 0
                        elif lst[ny][nx] == '.':
                            lst[ny][nx] = 'D'

    return 1

result = find()
print(result)

if result:
    for line in lst:
        print(''.join(line))