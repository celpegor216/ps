from collections import deque


M, N = map(int, input().split())
# 1인 경우 진우가 갈 수 있는 칸을 의미하고 0인 경우 진우가 갈 수 없는 칸
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque()
q.append((0, 0))

used = [[0] * M for _ in range(N)]
used[0][0] = 1

while q:
    y, x = q.popleft()

    if y == N - 1 and x == M - 1:
        print('Yes')
        break

    # 동쪽(오른쪽) 또는 남쪽(아래쪽)으로만 이동
    for dy, dx in ((0, 1), (1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
            q.append((ny, nx))
            used[ny][nx] = 1
else:
    print('No')