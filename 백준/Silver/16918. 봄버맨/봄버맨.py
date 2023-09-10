# 힌트: T % 4 기준으로 반복이 아님
# 힌트: T=1, T%2=0, T%4=3, T>1 and T&4=1

from collections import deque

N, M, T = map(int, input().split())
lst = [input() for _ in range(N)]
lst_24 = ['O' * M for _ in range(N)]

def check(bs):
    result = []

    q = deque()
    used = [[0] * M for _ in range(N)]

    for y, x in bs:
        q.append((y, x))
        used[y][x] = 1

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                used[ny][nx] = 1

    for n in range(N):
        tmp = ''
        for m in range(M):
            if used[n][m]:
                tmp += '.'
            else:
                tmp += 'O'
        result.append(tmp)

    return result


bombs = []
for n in range(N):
    for m in range(M):
        if lst[n][m] == 'O':
            bombs.append((n, m))

lst_3 = check(bombs)

bombs = []
for n in range(N):
    for m in range(M):
        if lst_3[n][m] == 'O':
            bombs.append((n, m))

lst_1 = check(bombs)


if T == 1:
    for line in lst:
        print(line)
elif T % 2 == 0:
    for line in lst_24:
        print(line)
elif T % 4 == 3:
    for line in lst_3:
        print(line)
else:
    for line in lst_1:
        print(line)