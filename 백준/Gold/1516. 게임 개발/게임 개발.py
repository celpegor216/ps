from collections import deque

N = int(input())

time = [0] * (N + 1)
results = [0] * (N + 1)
parent = [0] * (N + 1)
children = [[] for _ in range(N + 1)]

for n in range(N):
    tmp = list(map(int, input().split()))

    time[n + 1] = tmp[0]
    parent[n + 1] += len(tmp) - 2
    for p in tmp[1:]:
        if p == -1:
            break

        children[p].append(n + 1)

q = deque()
for n in range(1, N + 1):
    if not parent[n]:
        q.append(n)

while q:
    now = q.popleft()

    if not parent[now]:
        results[now] += time[now]

    for child in children[now]:
        results[child] = max(results[child], results[now])
        parent[child] -= 1

        if parent[child] == 0:
            q.append(child)

for result in results[1:]:
    print(result)