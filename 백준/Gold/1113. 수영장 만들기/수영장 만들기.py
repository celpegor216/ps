# 반례 참고
# 가장자리에 닿았는지 체크할 때 처음에는 0만 고려했는데 N - 1, M - 1도 고려해야 함
# 자기보다 작은 게 있어도 연결된 칸을 모두 방문체크 하고 나와야 함


from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

pos = [[] for _ in range(10)]

for i in range(1, N - 1):
    for j in range(1, M - 1):
        pos[lst[i][j]].append((i, j))

def bfs(y, x, i):
    used[y][x] = 1

    q = deque()
    q.append((y, x))

    min_maxv = 9
    has_border = 0
    has_lower = 0

    idx = 0
    while idx < len(q):
        y, x = q[idx]

        # 가장자리에 닿은 경우 물을 채울 수 없음
        if not (0 < y < N - 1 and 0 < x < M - 1):
            has_border = 1

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx]:
                continue

            # 본인보다 작은 값이 근처에 있을 경우 물을 채울 수 없음
            if lst[ny][nx] < i:
                has_lower = 1
            elif lst[ny][nx] > i:
                min_maxv = min(min_maxv, lst[ny][nx])
            elif lst[ny][nx] == i:
                used[ny][nx] = 1
                q.append((ny, nx))

        idx += 1

    if has_border or has_lower:
        return 0

    res = (min_maxv - i) * len(q)

    while q:
        y, x = q.popleft()
        lst[y][x] = min_maxv

    return res


result = 0
for i in range(1, 9):
    used = [[0] * M for _ in range(N)]

    for y, x in pos[i]:
        if used[y][x]:
            continue

        result += bfs(y, x, i)

print(result)