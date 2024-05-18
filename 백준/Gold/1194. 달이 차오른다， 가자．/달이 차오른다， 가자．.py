# 해답: https://baby-ohgu.tistory.com/53

from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

q = deque()
used = [[[0] * 2 ** 6 for _ in range(M)] for _ in range(N)]

for n in range(N):
    if q:
        break

    for m in range(M):
        if lst[n][m] == '0':
            q.append((n, m, 0, 0))
            used[n][m][0] = 1
            break

result = -1

while q:
    nowy, nowx, nowc, keys = q.popleft()

    if lst[nowy][nowx] == '1':
        result = nowc
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx][keys]:
            if lst[ny][nx] == '#':
                continue

            if 'A' <= lst[ny][nx] <= 'F' and not keys & 1 << (ord(lst[ny][nx]) - ord('A')):
                continue
            
            if 'a' <= lst[ny][nx] <= 'f':
                q.append((ny, nx, nowc + 1, keys | 1 << (ord(lst[ny][nx]) - ord('a'))))
                used[ny][nx][keys | 1 << (ord(lst[ny][nx]) - ord('a'))] = 1
            else:
                q.append((ny, nx, nowc + 1, keys))
                used[ny][nx][keys] = 1

print(result)