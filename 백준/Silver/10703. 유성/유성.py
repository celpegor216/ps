from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

stars = [-1] * M
lands = [N] * M
stars_pos = []

def find(char):
    q = deque()
    used = [[0] * M for _ in range(N)]

    if char == 'X':
        flag = 1

        for n in range(N):
            if flag:
                for m in range(M):
                    if lst[n][m] == char:
                        q.append((n, m))
                        used[n][m] = 1
                        stars_pos.append((n, m))
                        flag = 0
                        break
    else:
        q.append((N - 1, M - 1))
        used[-1][-1] = 1

    while q:
        nowy, nowx = q.popleft()

        if char == 'X' and stars[nowx] < nowy:
            stars[nowx] = nowy
        elif char == '#' and lands[nowx] > nowy:
            lands[nowx] = nowy
        
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == char:
                used[ny][nx] = 1
                if char == 'X':
                    stars_pos.append((ny, nx))
                q.append((ny, nx))
    
find('X')
find('#')

moves = 21e8
for m in range(M):
    if stars[m] > -1 and lands[m] - stars[m] < moves:
        moves = lands[m] - stars[m]

result = [['.'] * M for _ in range(N)]
for n in range(min(lands), N):
    for m in range(M):
        if lst[n][m] == '#':
            result[n][m] = '#'

for pos in stars_pos:
    result[pos[0] + moves - 1][pos[1]] = 'X'

for line in result:
    print(''.join(line))