from collections import deque

N, M, K = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[[21e8] * (K + 1) for _ in range(M)] for _ in range(N)]
used[0][0][0] = 1

q = deque()
q.append((0, 0, 0, 1))

while q:
    nowy, nowx, nowk, nowc = q.popleft()

    if nowy == N - 1 and nowx == M - 1:
        continue

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == '0' and used[ny][nx][nowk] > nowc + 1:
                used[ny][nx][nowk] = nowc + 1
                q.append((ny, nx, nowk, nowc + 1))
            elif lst[ny][nx] == '1' and nowk + 1 <= K and used[ny][nx][nowk + 1] > nowc + 1:
                used[ny][nx][nowk + 1] = nowc + 1
                q.append((ny, nx, nowk + 1, nowc + 1))

result = 21e8

for item in used[-1][-1]:
    if result > item:
        result = item

if result == 21e8:
    print(-1)
else:
    print(result)