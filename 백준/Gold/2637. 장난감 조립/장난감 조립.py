from collections import deque

N = int(input())
M = int(input())

parents = [0] * (N + 1)
children = [[] for _ in range(N + 1)]
parts = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, k = map(int, input().split())
    parents[x] += 1
    children[y].append([x, k])

q = deque()
results = []

for n in range(1, N + 1):
    if not parents[n]:
        q.append(n)
        results.append(n)
        parts[n][n] += 1

while q:
    n = q.popleft()

    for x, k in children[n]:
        parents[x] -= 1

        for p in range(1, N + 1):
            parts[x][p] += parts[n][p] * k
        
        if not parents[x]:
            q.append(x)

for n in results:
    print(n, parts[-1][n])