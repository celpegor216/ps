from collections import deque

N, M = map(int, input().split())

parents = [0] * (N + 1)
children = [[] for _ in range(N + 1)]

for m in range(M):
    lst = list(map(int, input().split()))

    for i in range(1, lst[0]):
        children[lst[i]].append(lst[i + 1])
        parents[lst[i + 1]] += 1

result = []

q = deque()

for i in range(1, N + 1):
    if not parents[i]:
        q.append(i)
        result.append(i)

while q:
    now = q.popleft()

    for child in children[now]:
        parents[child] -= 1

        if not parents[child]:
            q.append(child)
            result.append(child)

if len(result) == N:
    for item in result:
        print(item)
else:
    print(0)