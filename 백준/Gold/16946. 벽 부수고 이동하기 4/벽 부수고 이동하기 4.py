from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

group = [[(x, y) for y in range(M)] for x in range(N)]
used = [[0] * M for _ in range(N)]
cnt = dict()
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

for i in range(N):
    for j in range(M):
        if lst[i][j] == '0' and not used[i][j]:
            q = deque()
            q.append((i, j))

            used[i][j] = 1

            while q:
                nowy, nowx = q.popleft()

                group[nowy][nowx] = (i, j)
                cnt[(i, j)] = cnt.get((i, j), 0) + 1

                for dy, dx in d:
                    ny, nx = nowy + dy, nowx + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '0':
                        q.append((ny, nx))
                        used[ny][nx] = 1

for i in range(N):
    for j in range(M):
        if lst[i][j] == '1':
            tmp = set()

            for dy, dx in d:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '0':
                    tmp.add(group[ny][nx])
            
            result = 1
            for key in tmp:
                result += cnt[key]
            
            print(result % 10, end='')
        else:
            print(0, end='')
    print()