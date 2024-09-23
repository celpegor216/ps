TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    lst = [['*'] * (M + 4) for _ in range(N + 4)]
    for i in range(1, N + 3):
        lst[i][1] = '.'
        lst[i][-2] = '.'
    for j in range(1, M + 3):
        lst[1][j] = '.'
        lst[-2][j] = '.'

    for i in range(2, N + 2):
        tmp = input()
        for j in range(2, M + 2):
            lst[i][j] = tmp[j - 2]

    keys = input()
    if keys == '0':
        keys = ''

    q = [(1, 1)]
    used = [[0] * (M + 4) for _ in range(N + 4)]
    used[1][1] = 1

    while q:
        nq = []

        for y, x in q:
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if lst[ny][nx] == '*' or used[ny][nx]:
                    continue

                if lst[ny][nx].isupper() and lst[ny][nx].lower() not in keys:
                    continue

                if lst[ny][nx].islower() and lst[ny][nx] not in keys:
                    keys += lst[ny][nx]
                    used = [[0] * (M + 4) for _ in range(N + 4)]

                used[ny][nx] = 1
                nq.append((ny, nx))

        q = nq

    result = 0
    for i in range(2, N + 2):
        for j in range(2, M + 2):
            if lst[i][j] == '$' and used[i][j]:
                result += 1

    print(result)