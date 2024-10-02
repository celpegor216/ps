from collections import deque

N, W, P = map(int, input().split())

# y, x, t
workers = [list(map(int, input().split())) for _ in range(W)]

# 컨베이어 벨트 경로
path = []
for j in range(N):
    path.append((0, j))
for i in range(1, N):
    path.append((i, N - 1))
for j in range(N - 2, -1, -1):
    path.append((N - 1, j))
L = len(path)

q = deque([0] * L)
work_until = [0] * W
possible_positions = [[] for _ in range(W)]
for w in range(W):
    y, x = workers[w][:2]
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if (ny, nx) in path:
            possible_positions[w].append(path.index((ny, nx)))
    possible_positions[w].sort(reverse=True)

result = 0
for time in range(P + L):
    q.pop()

    if P:
        q.appendleft(1)
        P -= 1
    else:
        q.appendleft(0)

    for w in range(W):
        if work_until[w] > time:
            continue

        for idx in possible_positions[w]:
            if q[idx]:
                q[idx] = 0
                work_until[w] = time + workers[w][-1]
                result += 1
                break

print(result)